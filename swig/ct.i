%module libct
%{
  #include <ct.h>
%}

%rename ("%(strip:[ct_])s") "";
%include <ct.h>
