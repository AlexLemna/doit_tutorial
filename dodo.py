from doit.tools import run_once


def task_hello_world():
    return {"actions": ['echo "hello world!" > hello.txt'], "targets": ["hello.txt"]}


def task_download_data():
    return {
        "actions": [
            "curl -OL https://s3.amazonaws.com/pydoit-intermediate/Melee_data.csv.gz"
        ],
        "targets": ["Melee_data.csv.gz"],
        "uptodate": [run_once],
    }


def task_gunzip_data():
    return {
        "actions": ["gunzip -c %(dependencies)s > %(targets)s"],
        "targets": ["Melee_data.csv"],
        "file_dep": ["Melee_data.csv.gz"],
    }


def task_plot_heatmap():
    def do_plot(dependencies, targets):
        import matplotlib.pyplot as plt
        import pandas as pd
        import seaborn as sns

        data = pd.read_csv(list(dependencies)[0], index_col=0)
        clst = sns.clustermap(
            data,
            linewidths=0.5,
            figsize=(8, 8),
            square=True,
            method="ward",
            z_score=0,
            row_cluster=False,
        )
        # We like pretty charts, so rotate the labels
        plt.setp(clst.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
        plt.setp(clst.ax_heatmap.xaxis.get_majorticklabels(), rotation=90)
        clst.savefig(targets[0])

    return {
        "actions": [do_plot],
        "file_dep": ["Melee_data.csv"],
        "targets": ["Melee_data.csv.heatmap.pdf"],
    }
