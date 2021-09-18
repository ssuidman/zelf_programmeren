import Server
import pandas as pd
import numpy as np
from tqdm import tqdm

responses = pd.read_csv('walks.csv', sep=",")

if __name__ == '__main__':

    print(responses)
    print('🪂 Total participants:', len(responses))
    print('🪃 Peers to be matched:', (len(responses) / 2))
    print('🥌 Starting e-mail server.')

    for index, row in tqdm(responses.iterrows(), total=responses.shape[0]):
        server.send_mail(
                  row['email'],
                  row['name'],
                  row['name_peer'],
                  row['faculty_peer'],
                  row['email_peer'],
                  row['phone_peer'],
                  [])

    print('🎉 E-mail processing complete.')