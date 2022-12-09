import subprocess

out = subprocess.Popen(['pesq', '+16000', '+wb', 'parole16.wav', 'merged.wav_-10.0dB.wav'], 
    stdout = subprocess.PIPE, 
    stderr = subprocess.STDOUT)

print(out)

stdout, stderr = out.communicate()
outStr = str(stdout)
measureResultStr = outStr.split(' ')[-1].replace("\\n","").replace("\\r","").replace("\"","")
print(measureResultStr)