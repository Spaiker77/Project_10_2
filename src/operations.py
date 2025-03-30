import re
from collections import Counter
from typing import List, Dict


def filter_by_description(transactions: List[Dict], search: str) -> List[Dict]:
    """Фильтрует транзакции по строке в описании"""
    if not transactions or not search:
        return []

    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get('description', ''))]


def count_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Считает операции по категориям"""
    if not transactions or not categories:
        return {}

    counts = Counter(t['description'] for t in transactions if 'description' in t)
    return {cat: counts.get(cat, 0) for cat in categories}