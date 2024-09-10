from airflow.decorators import dag, task
from airflow.utils.dates import days_ago


@dag(
    start_date=days_ago(1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "RINTIO", "retries": 3},
    tags=["scraper", "ai_agent"],
)
def sublime_benin_data_collect():
    @task
    def task_1():
        pass

    @task
    def task_2():
        pass

    @task
    def task_3():
        pass

    @task
    def task_4():
        pass

    @task
    def task_6():
        pass

    @task
    def task_7():
        pass

    # Define task dependencies
    t1 = task_1()
    t2 = task_2()
    t3 = task_3()
    t4 = task_4()
    t6 = task_6()
    t7 = task_7()

    t1 >> [t2, t3, t4, t6, t7]


# Instantiate the DAG
sublime_benin_data_collect()
