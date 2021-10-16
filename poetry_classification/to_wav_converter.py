import os
import pandas as pd
from pydub import AudioSegment

metadata = pd.read_excel("./جدول جميع الأبيات .xlsx")
for file_path in metadata["Utterance name"]:
    complete_path = f"dataset/{file_path}"
    if os.path.exists(complete_path):
        complete_wav_path = f"dataset_wav/{file_path}"
        # os.system(f'ffmpeg -i {complete_path} {complete_wav_path}')
        audio = AudioSegment.from_file(complete_path)
        audio.export(f"dataset_wav/{file_path}", format="wav")
