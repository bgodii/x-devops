"""Example DAG demonstrating the usage of dynamic task mapping."""
from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id="dynamic_task_mapping",
    start_date=datetime(2022, 3, 4),
    schedule_interval="@once",

) as dag:
    @task
    def add_one(x: int):
        return x + 1

    @task
    def sum_it(values):
        total = sum(values)
        print(f"List values: {values}")
        print(f"Total was {total}")
        return total
    
    @task
    def add(x: int, y: int):
        return x + y
    
    added_values = add_one.expand(x=[1, 2, 3])
    result = sum_it(added_values)
    added_ten = add.partial(y=result).expand(x=added_values)
    sum_it(added_ten)
