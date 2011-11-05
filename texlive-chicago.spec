# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/chicago
# catalog-date 2008-12-25 20:17:19 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-chicago
Version:	20081225
Release:	1
Summary:	A "Chicago" bibliography style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/chicago
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chicago.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
Chicago is a BibTeX style that follows the "B" reference style
of the 13th Edition of the Chicago manual of style; a LaTeX
package (to LaTeX 2.09 conventions) is also provided. The style
was derived from the newapa style.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/chicago/chicago.bst
%{_texmfdistdir}/tex/latex/chicago/chicago.sty
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
