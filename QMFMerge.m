function [] = QMFMerge(reconstructionFileName, lowbandFileName, highbandFileName)

% projektowanie filtru, mozna pominac gdy znamy odp. impulsowa h0
dv=0.00003; % dla mniejszych wartosci nie dziala prawidllowo
[N,fpts,mag,wt]=firpmord([0.395 0.605],[1 0],[dv dv]);
 N=floor(N/2)*2;

[q,err]=firpm(N,fpts,mag,wt);

q(1+floor(N/2))=q(1+floor(N/2))+err;
h0=firminphase(q);    % tu mamy odp, impulsowa, mozna ja wczytac z pliku jesli projektowanie nie dziala
g0=fliplr(h0);
k=0:(N/2);
h1=((-1).^k).*g0;
g1=-((-1).^k).*h0;

h0=h0*sqrt(2);
g0=g0*sqrt(2);
h1=h1*sqrt(2);
g1=g1*sqrt(2);

% [H0,w0] = freqz(h0,1,256);
% [H1,w1] = freqz(h1,1,256);
% [G0,w2] = freqz(g0,1,256);
% [G1,w3] = freqz(g1,1,256);

% mamy 2 filtry analizy i 2 filtry syntezy

% v0=conv(h0,x);    % filtracja przez splot
% u0=downsample(v0,2);  % sygnal dolnopasmnowy - do kwantyzacji
% len_low=length(u0)
%  nom1 = [fichier '_low.wav'];  % nazwa
%  wavwrite(u0,fe/2,nom1);   % zapisujemy sygnal dolnopasmowy jako sygnal 8000 pr/s
% % tu mozna wstawic koder sygnalu dolnopasmowego
% G7231Coder_basic(nom1,'d.dat');
% G7231Decoder_3('d.dat','lowd.wav');
% % u0_   - sygnal skwantowany
%u0_=wavread('lowd.wav');

[u0_, fs0_] =wavread(lowbandFileName);
d0=upsample(u0_,2);
y0=conv(d0,g0);

% v1=conv(h1,x);
% u1=downsample(v1,2); % sygnal gornopasmowy - do kwantyzacji
% len_high=length(u1)
%  nom2 = [fichier '_high.wav'];  % nazwa
%  wavwrite(u1,fe/2,nom2);   % zapisujemy sygnal gornopasmowy jako sygnal 8000 pr/s
% % tu mozna wstawic koder sygnalu gornopasmowego
% G7231Coder_basic(nom2,'dd.dat');
% G7231Decoder_3('dd.dat','highd.wav');
% % u1_   - sygnal skwantowany
% u1_=wavread('highd.wav');
%u1_=zeros(size(u1_));  % ta instrukcja zeruje gorny kanal
u1_=wavread(highbandFileName);
d1=upsample(u1_,2);
y1=conv(d1,g1);

% figure(2);
% subplot(211)
% plot(u0,'b'),title('sygnal dolnopasmowy u0');
% subplot(212)
% plot(u1,'g'),title('sygnal gornopasmowy u1');
len=min([length(y0), length(y1)])
y=y0(1:len)+y1(1:len);   %  sygnal wyjsciowy


% M=512;
% [X,w4] = freqz(x,1,M);
% [Y,w7] = freqz(y,1,M);
% [V0,w5] = freqz(y0,1,M);
% [V1,w6] = freqz(y1,1,M);



% figure(3);
% subplot(2,1,1);
% plot(w4/pi,abs(X),'g'),title('widmo syg. we/wy');xlabel('\omega/\pi'); ylabel('Magnitude');grid;
% hold on
% plot(w7/pi,abs(Y),'r'),title('widmo syg. we/wy');xlabel('\omega/\pi'); ylabel('Magnitude');grid;
% subplot(2,1,2);
% plot(w5/pi,20*log( abs(V0) ),'b'),title('widmo U0/U1');xlabel('\omega/\pi'); ylabel('dB');grid;
% hold on
% plot(w6/pi,20*log( abs(V1) ),'m'),title('widmo U0/U1');xlabel('\omega/\pi'); ylabel('dB');grid;

% m=length(y)-N;
% x=x(1:m,1);

% nst=N/2;
% figure(4);
% subplot(211)
% plot(1:length(x),x)
% title('sygnal wejsciowy')
% subplot(212)
% plot(y(nst+1:nst+m))
% title('sygnal wyjsciowy')
% esig=x-y(nst+1:nst+m);
% gain=norm(x)/norm(y(nst+1:nst+m))
% ycor=y(nst+1:nst+m)*gain;
% er=norm(x-ycor)  % miara bledu

% qerr=x-ycor;
% figure(11)
% plot(qerr) 
% title('sygnal bledu')

% figure(12),hold off
% plot(h0,'b'),hold on
% plot(g0,'g')
% plot(h1,'r')
% plot(g1,'m')
% title('odpowiedzi impulsowe')

%  snr_(x(20:m),ycor(20:m));  % porownanie we - wy
% % 
% figure(13), hold off
% plot(x), hold on
% plot(ycor, 'g')
% plot(qerr, 'r')
% title('we, wy i blad kwantyzacji')

wavwrite(y,fs0_*2 ,reconstructionFileName);
% wavwrite(ycor,fe,reconstructionFileName);   % zapisujemy sygnal wyjsciowy
% wavwrite(x,fe,nom4);   % zapisujemy sygnal wejsciowy
% wavwrite(x-ycor,fe,nom5);   % zapisujemy sygnal bledu

end