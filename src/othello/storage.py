import json
import os
from typing import Dict, Any, Optional

class JSONStorage:
    """JSONのファイルを操作する。プレイヤーごとの試合数・勝ち・負け・引き分けを記録する"""
    def __init__(self, file_path: str = "PlayerRecordStorage.json"):
        self.file_path = file_path

    def exists(self) -> bool:
        """記録ファイルが存在するかどうかを返す"""
        return os.path.exists(self.file_path)

    def load(self) -> Dict[str, Dict[str, int]]:
        """
        JSONファイルから全プレイヤーのレコードを読み込んで返す
        ファイルが無ければ空の辞書を返す。破損している場合は上書きして空辞書を返す
        レコード形式:
          {
            "player_name": {"matches": int, "wins": int, "losses": int, "draws": int},
            ...
          }
        """
        if not self.exists():
            return {}

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, dict):
                return {}
            normalized: Dict[str, Dict[str, int]] = {}
            for name, rec in data.items():
                if not isinstance(rec, dict):
                    rec = {}
                normalized[name] = {
                    "matches": int(rec.get("matches", 0)),
                    "wins": int(rec.get("wins", 0)),
                    "losses": int(rec.get("losses", 0)),
                    "draws": int(rec.get("draws", 0)),
                }
            return normalized
        except (json.JSONDecodeError, ValueError):
            try:
                with open(self.file_path, "w", encoding="utf-8") as f:
                    json.dump({}, f, ensure_ascii=False, indent=2)
            except Exception:
                pass
            return {}

    def save(self, records: Dict[str, Dict[str, int]]) -> None:
        """辞書をJSONファイルに保存する（整形して書き込む）"""
        tmp_path = f"{self.file_path}.tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, self.file_path)

    def get_player_record(self, player_name: str) -> Dict[str, int]:
        """指定プレイヤーのレコードを返す（存在しなければゼロで初期化したレコードを返す）。"""
        records = self.load()
        if player_name not in records:
            records[player_name] = {"matches": 0, "wins": 0, "losses": 0, "draws": 0}
        return records[player_name]

    def record_match(self, player1: str, player2: str, winner: Optional[str]) -> None:
        """
        1試合の結果を記録する。
        - 引き分けの場合: winner に None を渡す -> 両者の matches と draws を +1
        - 勝者がある場合: winner は勝者の名前 (player1 または player2) を渡す
          -> 勝者 wins+1, 敗者 losses+1, 両者 matches+1
        保存は内部で行う。
        """
        if player1 == player2:
            # 同一プレイヤー対戦の記録は無視または例外にする（ここでは無視）
            return

        records = self.load()

        # 保証: 両プレイヤーのレコードを存在させる
        for name in (player1, player2):
            if name not in records or not isinstance(records[name], dict):
                records[name] = {"matches": 0, "wins": 0, "losses": 0, "draws": 0}

        # 引き分け
        if winner is None:
            records[player1]["matches"] += 1
            records[player2]["matches"] += 1
            records[player1]["draws"] += 1
            records[player2]["draws"] += 1
        else:
            # 勝者が player1 または player2 のいずれかであることを期待する
            if winner not in (player1, player2):
                # 無効な勝者指定は無視
                return
            loser = player2 if winner == player1 else player1
            records[winner]["matches"] += 1
            records[loser]["matches"] += 1
            records[winner]["wins"] += 1
            records[loser]["losses"] += 1

        # 保存
        self.save(records)
