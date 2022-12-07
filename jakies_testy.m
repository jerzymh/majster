
[u, Fs] = audioread('diaboj.wav');
N   = 4;
G   = 3; % 1 dB
Wo1 = 0;
Wo2 = 1; % Corresponds to Fs/2 (Hz) or pi (rad/sample)
BW = 1000/(Fs/2); % Bandwidth occurs at 7.4 dB in this case
[B1,A1] = designParamEQ(N,G,Wo1,BW,'Orientation','row');
[B2,A2] = designParamEQ(N,G,Wo2,BW,'Orientation','row');
BQ1 = dsp.SOSFilter('Numerator',B1,'Denominator',A1);
BQ2 = dsp.SOSFilter('Numerator',B2,'Denominator',A2);
%hfvt = fvtool(BQ1,BQ2,'Fs',Fs,'Color','white');
%legend(hfvt,'Low Shelf Filter','High Shelf Filter');

y = BQ2(u);
figure(3)
plot(abs(fft(u)))
grid on
figure(4)
plot(abs(fft(y)))
grid on