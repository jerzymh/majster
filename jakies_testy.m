[u, Fs] = audioread('diaboj.wav');
N   = 4;
G1  = 20; % 3 dB
G2  = -20;% -3 dB
Wo1 = 0;
Wo2 = 1; % Corresponds to Fs/2 (Hz) or pi (rad/sample)
BW = 1000/(Fs/2); % Bandwidth occurs at 7.4 dB in this case
[B1,A1] = designParamEQ(N,G1,Wo1,BW,'Orientation','row');
[B2,A2] = designParamEQ(N,G1,Wo2,BW,'Orientation','row');
[B3,A3] = designParamEQ(N,G2,Wo2,BW,'Orientation','row');
BQ1 = dsp.SOSFilter('Numerator',B1,'Denominator',A1);
BQ2 = dsp.SOSFilter('Numerator',B2,'Denominator',A2);
BQ3 = dsp.SOSFilter('Numerator',B3,'Denominator',A3);
%hfvt = fvtool(BQ1,BQ2,'Fs',Fs,'Color','white');
%legend(hfvt,'Low Shelf Filter','High Shelf Filter');

y = BQ2(u);
r = BQ3(y);
figure(3)
plot(abs(fft(u)))
set(gca, 'YScale', 'log');
grid on
figure(4)
plot(abs(fft(y)))
set(gca, 'YScale', 'log');
grid on
figure(5)
plot(abs(fft(r)))
set(gca, 'YScale', 'log');
audiowrite('a.wav',y,Fs)