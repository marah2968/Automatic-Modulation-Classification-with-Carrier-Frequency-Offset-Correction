function shaped_framed=shape_frame(x)
energy=sum(abs(x).^2); %time domain


x=x./energy;
shaped_frame=zeros(1,size(x,2)*2,size(x,1),1);

I=real(x);
Q=imag(x);


%I = permute(I,[2 1]);
%Q = permute(Q,[2 1]);

nt=size(x,2);

shaped_frame(1,1:nt,:)=I';
shaped_frame(1,nt+1:2*nt,:)=Q';
shaped_framed=shaped_frame;





end