function [] = HighbandBoost(sourceFileName, resultFileName, leveldB)

[u, Fs] = audioread(sourceFileName);

N   = 4;
G1  = leveldB; % level dB
Wo2 = 1; % Corresponds to Fs/2 (Hz) or pi (rad/sample)
BW = 1000/(Fs/2); % Bandwidth occurs at 7.4 dB in this case
[B,A] = designParamEQ(N,G1,Wo2,BW,'Orientation','row');
BQ = dsp.SOSFilter('Numerator',B,'Denominator',A);
%hfvt = fvtool(BQ1,BQ2,'Fs',Fs,'Color','white');
%legend(hfvt,'Low Shelf Filter','High Shelf Filter');

y = BQ(u);

audiowrite(resultFileName,y,Fs);