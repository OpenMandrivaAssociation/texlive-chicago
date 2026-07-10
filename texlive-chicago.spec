%global tl_name chicago
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A Chicago bibliography style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/chicago
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chicago.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Chicago is a BibTeX style that follows the "B" reference style of the
13th Edition of the Chicago manual of style; a LaTeX package (to LaTeX
2.09 conventions) is also provided. The style was derived from the
newapa style.

