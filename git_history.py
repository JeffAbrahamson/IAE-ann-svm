#!/usr/bin/env python3

"""
Show git history of student projects.

To create the repos locally, I did this in the course directory:

    grep repo projects.md | sed -e 's/^.*(/git clone /; s/)//;'

I then added more descriptive names for myself.

Running this assumes I've updated (pulled) all the local repos.

"""

import datetime
import git
import matplotlib.pyplot as plt
import numpy as np

def repo_get_commits(repo_name):
    """Get the commits in one repo, return a sorted array of commit timestamps.
    """
    repo = git.Repo(repo_name)
    # Use a set because branches often overlap.
    timestamps = set()
    for branch in repo.branches:
        for commit in branch.commit.iter_parents():
            timestamps.add(commit.authored_datetime)
    return sorted(list(timestamps))

def main():
    """Plot some git commits.

    git clone https://github.com/Kyllien/Jane-Street-Market-Prediction JBD+KR
    git clone https://github.com/ThibaultBregal/projet-SVM GS+TB
    git clone https://github.com/AmauMaill/Cassava-Leaf-Disease-Classification AM+VF
    git clone https://github.com/AndreAng1/SVM-ANN-Andre-M2-EKAP AA+SB
    git clone https://github.com/astridval/G2Net-Gravitational-Wave-Detection AV+BL
    git clone https://github.com/AntoinePetiteau/Brain-Tumor-Radiogenomic-Classification LLM+AP
    git clone https://github.com/Sara-Louis/Sara-Meziani-et-Louis-Mortreuil SM+LM
    git clone https://github.com/Achille1/Projet_M2_Chaii-Hindi_and_Tamil_Question_Answering MK+AS
    git clone https://github.com/LucieVrignaud/Projet-M2-EKAP-Mocher-Vrignaud LV+CM
    git clone https://github.com/lcorven/PROJET_M2_EKAP_CHIFFOLEAU_CORVEN QC+LC

    """
    repo_names = ['amaury-maillard_vincent-fattorelli', 'andre-angwe_sory-barry',
                  'astrid-valicon_gabin-lagre', 'gwendal-suau_thibault-bregal',
                  'jean-baptiste-delchateau_kyllien-romand', 'luc-le-mée_antoine-petiteau',
                  'lucie-vrignaud_cécile-mocher', 'mohamed-kouyate_achille-siabi',
                  'quentin-chiffoleau_loïc-corven', 'sara-meziani_louis-mortreuil', ]
    time_series = []
    for repo_name in repo_names:
        time_series.append(repo_get_commits(repo_name))
    min_timestamp = min([min(series) for series in time_series if len(series) > 0])
    max_timestamp = max([max(series) for series in time_series if len(series) > 0])
    # Use two more than the days available to deal with times a bit
    # before or after first and last day.
    days_in_universe = (max_timestamp - min_timestamp).days + 2
    # Now I'd like each time series expressed as a sequence of floats
    # representing days since day 0.
    day_series = []
    for series in time_series:
        day_series.append([(d - min_timestamp).days + (d - min_timestamp).seconds / 3600. / 24.
                           for d in series])
    plt.xlim(0, days_in_universe)
    plt.xticks(np.arange(days_in_universe))
    plt.yticks(np.arange(len(repo_names)), repo_names)
    for index, series in enumerate(day_series):
        plt.scatter(series, [index] * len(series))
    plt.show()

if __name__ == '__main__':
    main()
