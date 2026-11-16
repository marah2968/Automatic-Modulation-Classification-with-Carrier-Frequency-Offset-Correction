clc;
clear all;
addpath('modulators', 'channeling');
% Parameters
snrsDb =[0];
%snrsDb = 0;
%rng(10000);
cfos =[]; % degrees
%cfos=0;
%ph_imbs =[-10:2:10]; % degrees

frame_length = 128;
sps = 8;
symbol_sample =8;
number_of_symbol = frame_length / sps;
maxNumberSignals =10;
fs=200000;
dfc=[-10:1:10];
Ts=1/fs;
applyRayleigh=false;
applyRicean=true;


% Initialize data structures
ds1 =struct();
ds2 =struct();
ds3 =struct();

modulationTypes=categorical(["CPFSK"]);
m=0;
% Outer loop for generating signals
for i = 1:maxNumberSignals
    
    dataSource = getDataSource(modulationTypes(1), symbol_sample, frame_length, fs);
    modulator = getModulator(modulationTypes(1), symbol_sample, fs);
    for snrVal = 1:length(snrsDb)

        for cfo = 1:length(cfos)
          % Initialize data source and modulator based on modulation type

             
            % Generate or load data
            x = dataSource();
            
            % Modulate the data
             y = modulator(x);
            z=y;

                            %add multipath fading
                            if applyRicean==true
                                display(1);
                                y=riceanMultipath(y,fs);
                            elseif applyRayleigh==true
                                y=rayleighMultipath(y,fs);
                            end


            % Apply  frequency offset
 pfo = comm.PhaseFrequencyOffset('SampleRate',fs,'FrequencyOffset',cfos(cfo)*50);
                            y_f=pfo(y);
                            y=y_f;            
            % Add AWGN
             rxSamples = awgn(y, snrsDb(snrVal), 'measured');
            
            % Shape the received frame
             frameshaped = shape_frame(rxSamples);
            
            % Store the data in ds and ds1
                        label={string(modulationTypes(1)),i,snrsDb(snrVal),cfos(cfo),-100,-100,-100};
% 
              key = join(string(label), 'r');
              key2=join(string(label), 'r');
              key = strrep(key, '-', 'n');
             key2= strrep(key2, '-', 'n');
% 
%              value = zeros(Ns, 2 * Nts, sample_length);
              value = frameshaped;
              ds1 = setfield(ds1, key, value);
%             
%             % Store cfo in ds1
             value2 = cfos(cfo)*50;
              ds2 = setfield(ds2, key2, value2);
             value3=snrsDb(snrVal);
              ds3 = setfield(ds3, key2, value3);


        end
    end
    i=i+1;
end

%save('WBFM1.mat','ds1','-v7.3');
%save('WBFM2.mat','ds2','-v7.3');

%save('WBFM3.mat','ds3','-v7.3');

load('WBFM1.mat')





%%
figure;
plot(real(y));
hold on 
plot(imag(y));
