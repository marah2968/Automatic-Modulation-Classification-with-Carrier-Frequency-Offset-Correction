function y = qam16Modulator(x,sps)
%modulates the input x, and returns the root-raised cosine pulse shaped
%signal y. Input signal must be column vector of value in the set [0 15].
%Root-raised cosine filter has a roll-off factor 0.35 and spans 4 symbols. 
%The output signal y has unit power
%persistent filterCoeffs
%if isempty(filterCoeffs)
    filterCoeffs=rcosdesign(0.35,4,sps);
%end
syms=qammod(x,16,'gray', 'InputType','integer','UnitAveragePower',true);

z=2.6879*conv(filterCoeffs,upsample(syms,8));
m=floor(length(filterCoeffs)/2);
y=z(1+m:end-m);


end