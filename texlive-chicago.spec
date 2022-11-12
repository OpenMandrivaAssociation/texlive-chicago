Name:		texlive-chicago
Version:	15878
Release:	1
Summary:	A "Chicago" bibliography style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/chicago
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chicago.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Chicago is a BibTeX style that follows the "B" reference style
of the 13th Edition of the Chicago manual of style; a LaTeX
package (to LaTeX 2.09 conventions) is also provided. The style
was derived from the newapa style.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/chicago/chicago.bst
%{_texmfdistdir}/tex/latex/chicago/chicago.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex %{buildroot}%{_texmfdistdir}
