from datetime import datetime
from typing import List
import json
import os

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
        """辞書形式に変換"""
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "draws": self.draws,
            "total_games": self.total_games,
            "win_rate": self.win_rate
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'PlayerRecord':
        """辞書から復元"""
        record = PlayerRecord(data["name"])
        record.wins = data.get("wins", 0)
        record.losses = data.get("losses", 0)
        record.draws = data.get("draws", 0)
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