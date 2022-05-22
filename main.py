import numpy as np
import matlab.engine

mlEng = matlab.engine.start_matlab()
[u, fs] = mlEng.audioread("04. Pikers - Beton.flac", nargout=2)
u = np.array(u)
u = u[:, 0]
print(u[0])

mlEng.audiowrite("output.wav", matlab.double(u), fs, nargout=0)

