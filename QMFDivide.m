function [] = QMFDivide(inputFileName, lowbandFileName, highbandFileName)
    % % Podzial sygnalu na dolno i gornopasmowy - filtry QMF
%close all;
%clear;
% projektowanie filtru, mozna pominac gdy znamy odp. impulsowa h0
dv=0.00003; % dla mniejszych wartosci nie dziala prawidllowo
[N,fpts,mag,wt]=firpmord([0.395 0.605],[1 0],[dv dv]);
 N=floor(N/2)*2;

[q,err]=firpm(N,fpts,mag,wt);
% N;


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

% figure(1);
% subplot(211)
% plot(w0/pi,abs(H0),'g',w1/pi,abs(H1),'r'),title('Analysis Filters');xlabel('\omega/\pi'); ylabel('Magnitude');grid;
% subplot(212)
% plot(w2/pi,abs(G0),'b',w3/pi,abs(G1),'m'),title('Synthesis Filters');grid;xlabel('\omega/\pi'); ylabel('Magnitude');

% m = input('Input Length = ');
% m=100    %liczba probek przetwarzanego sygnalu
% x=randn(1,m);    % sygnal gaussowski, oczywiscie bedzie zastapiony sygnalem mowy

%   nazwa pliku audio
%         fichier = input('plik audio  ','s');  % nazwa pliku bez rozszerzenia
%  nom_fichier = [fichier '.wav'];
%   x = wavread(nom_fichier);

[x, fe] = wavread(inputFileName);
  m=length(x) ;
  

v0=conv(h0,x);    % filtracja przez splot
u0=downsample(v0,2);  % sygnal dolnopasmnowy - do kwantyzacji
%len_low=length(u0)

 wavwrite(u0,fe/2, lowbandFileName);   % zapisujemy sygnal dolnopasmowy jako sygnal 8000 pr/s
% tu mozna wstawic koder sygnalu dolnopasmowego
% G7231Coder_basic(nom1,'d.dat');
% G7231Decoder_3('d.dat','lowd.wav');
% u0_   - sygnal skwantowany
% u0_=wavread('lowd.wav');
% d0=upsample(u0_,2);
% y0=conv(d0,g0);

v1=conv(h1,x);
u1=downsample(v1,2); % sygnal gornopasmowy - do kwantyzacji
% len_high=length(u1)

 wavwrite(u1,fe/2, highbandFileName);   % zapisujemy sygnal gornopasmowy jako sygnal 8000 pr/s
% tu mozna wstawic koder sygnalu gornopasmowego

end