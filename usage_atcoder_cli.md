# AtCoder CLI 使い方

## 新規コンテスト

atcoderのディレクトリに遷移したうえで

```cli

acc new {ABC◯◯◯}

```

## 問題の追加

コンテストのディレクトリに遷移したうえで

```cli

acc add

```

と打つと選択画面が出る

- 2024/06/02 典型90やるために問題選んで追加するように指定している

```cli

acc config default-task-choice inquire

```

- ABCでA-G全てのディレクトリが自動でできるように設定するには

```cli

acc config default-task-choice all

```

## コード記述

各レベルのディレクトリのmain.pyに記述

```python

# 各レベルのディレクトリ内で
code main.py

```

## サンプルケースでテスト

各レベルのディレクトリ内で

```python

ojt
# oj t -c "python main.py" のエイリアス

```

## 提出

```python
accs
# acc s -- main.py --language 5078 のエイリアス
# 5078はpypy

```
