import os
loc_in = "audio_data2"
loc_out = "audio_data"
l = len(os.listdir(loc_out))
for i, j in enumerate(os.listdir(loc_in), 1):
    os.rename(loc_in+"/"+j, loc_out+f"/{i+l}.wav")