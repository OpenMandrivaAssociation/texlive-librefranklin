%global tl_name librefranklin
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX support for the Libre-Franklin family of fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/librefranklin
License:	lppl ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/librefranklin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/librefranklin.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Libre Franklin is an interpretation and expansion based on the 1912
Morris Fuller Benton's classic, designed by Pablo Impallari, Rodrigo
Fuenzalida and Nhung Nguyen.

