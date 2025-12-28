from datetime import datetime
from typing import List, Dict, Optional
import json
import os

from .storage import JSONStorage


class PlayerRecord:
    """個別プレイヤーの対戦記録を管理"""
    def __init__(self, name: str):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0

    @property
    def total_games(self) -> int:
        """総試合数"""
        return self.wins + self.losses + self.draws

    @property
    def win_rate(self) -> float:
        """勝率（0.0-100.0）"""
        if self.total_games == 0:
            return 0.0
        return round((self.wins / self.total_games) * 100, 1)

    def to_dict(self) -> dict:
        """辞書形式に変換（保存用）"""
        return {
            "name": self.name,
            "matches": self.total_games,
            "wins": self.wins,
            "losses": self.losses,
            "draws": self.draws,
            "win_rate": self.win_rate
        }

    @staticmethod
    def from_dict(data: dict) -> 'PlayerRecord':
        """辞書から復元"""
        record = PlayerRecord(data.get("name", ""))
        record.wins = int(data.get("wins", 0))
        record.losses = int(data.get("losses", 0))
        record.draws = int(data.get("draws", 0))
        return record

    def report_result(self, result: int) -> None:
        """
        対戦結果を記録
        result: 0=勝ち, 1=負け, 2=引き分け
        """
        if result == 0:
            self.wins += 1
        elif result == 1:
            self.losses += 1
        elif result == 2:
            self.draws += 1

    def __repr__(self) -> str:
        return f"PlayerRecord(name={self.name}, wins={self.wins}, losses={self.losses}, draws={self.draws})"


class PlayerRecordManager:
    """
    PlayerRecord を名前で管理し、JSONStorage 経由で永続化する。
    - records: Dict[str, PlayerRecord]
    - storage: JSONStorage
    公開メソッド:
      - get(name) -> Optional[PlayerRecord]
      - create_or_get(name) -> PlayerRecord
      - update_result(name, result) -> PlayerRecord
      - all_records() -> List[PlayerRecord]
      - save(path: Optional[str]=None) -> None
      - load(path: Optional[str]=None) -> None
      - clear(path: Optional[str]=None) -> None
    """
    def __init__(self, storage: Optional[JSONStorage] = None, storage_path: Optional[str] = None):
        if storage is not None:
            self.storage = storage
        else:
            self.storage = JSONStorage(storage_path or "data/PlayerRecordStorage.json")
        self.records: Dict[str, PlayerRecord] = {}
        self.load()

    def get(self, name: str) -> Optional[PlayerRecord]:
        return self.records.get(name)

    def create_or_get(self, name: str) -> PlayerRecord:
        rec = self.records.get(name)
        if rec is None:
            rec = PlayerRecord(name)
            self.records[name] = rec
        return rec

    def update_result(self, name: str, result: int) -> PlayerRecord:
        """
        指定プレイヤーの結果を更新して保存する。
        result: 0=勝ち, 1=負け, 2=引き分け
        """
        rec = self.create_or_get(name)
        rec.report_result(result)
        self.save()
        return rec

    def all_records(self) -> List[PlayerRecord]:
        return list(self.records.values())

    def save(self, path: Optional[str] = None) -> None:
        """
        現在の `records` を JSON に保存する。
        path を指定すると一時的に別ファイルへ保存する（内部で新しい JSONStorage を使う）。
        """
        payload: Dict[str, Dict[str, int]] = {}
        for name, rec in self.records.items():
            payload[name] = {
                "matches": rec.total_games,
                "wins": rec.wins,
                "losses": rec.losses,
                "draws": rec.draws
            }

        if path:
            tmp_storage = JSONStorage(path)
            tmp_storage.save(payload)
        else:
            self.storage.save(payload)

    def load(self, path: Optional[str] = None) -> None:
        """
        JSON から読み込んで `records` を復元する。
        path を指定するとそちらから読み込む（内部で新しい JSONStorage を使う）。
        破損や未存在の場合は空の辞書にする。
        """
        storage = JSONStorage(path) if path else self.storage
        raw = storage.load()
        self.records = {}
        for name, rec in raw.items():
            if not isinstance(rec, dict):
                continue
            # storage の形式に合わせて復元（wins/losses/draws がキー）
            rec_data = {
                "name": name,
                "wins": rec.get("wins", 0),
                "losses": rec.get("losses", 0),
                "draws": rec.get("draws", 0)
            }
            self.records[name] = PlayerRecord.from_dict(rec_data)

    def clear(self, path: Optional[str] = None) -> None:
        """
        記録を全削除して保存する。
        path を指定するとそちら（別ファイル）に保存する。
        """
        self.records = {}
        if path:
            tmp_storage = JSONStorage(path)
            tmp_storage.save({})
        else:
            self.storage.save({})