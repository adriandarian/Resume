from pylatex import (
    Document,
    Package,
    Section,
    MiniPage,
    Tabular,
)
from pylatex.utils import NoEscape
from pylatex.base_classes import Environment, Command


class Tightemize(Environment):
    """Creates a tightemize environment for bullet points."""

    _latex_name = "tightemize"

    packages = [Package("paralist")]


if __name__ == "__main__":
    # Initialize the document
    doc = Document(documentclass="article")
    doc.packages.append(Package("geometry", options=["hmargin=0cm", "vmargin=0.5cm"]))
    doc.packages.append(Package("xcolor", options=["usenames", "dvipsnames"]))
    doc.packages.append(Package("hyperref", options="hidelinks"))
    doc.packages.append(Package("titlesec"))
    doc.packages.append(Package("textpos", options="absolute"))
    doc.packages.append(Package("babel", options="UKenglish"))
    doc.packages.append(Package("isodate", options="UKenglish"))
    doc.packages.append(Package("fontspec"))
    doc.packages.append(Package("xltxtra"))
    doc.packages.append(Package("xunicode"))
    doc.packages.append(Package("fontawesome"))
    doc.packages.append(Package("multicol"))
    doc.packages.append(Package("paralist"))

    # Colors
    doc.append(NoEscape(r"\definecolor{date}{HTML}{666666}"))
    doc.append(NoEscape(r"\definecolor{primary}{HTML}{2b2b2b}"))
    doc.append(NoEscape(r"\definecolor{headings}{HTML}{6A6A6A}"))
    doc.append(NoEscape(r"\definecolor{subheadings}{HTML}{333333}"))

    # Fonts
    doc.append(NoEscape(r"\defaultfontfeatures{Mapping=tex-text}"))
    doc.append(
        NoEscape(
            r"""
            \setmainfont[
                Path=./fonts/lato/,
                UprightFont=*-Reg,
                BoldFont=*-Bol,
                ItalicFont=*-RegIta,
                BoldItalicFont=*-BolIta,
                SmallCapsFont=*-Reg
            ]{Lato}
            """
        )
    )
    doc.append(
        NoEscape(
            r"""
            \setsansfont[
                Path=./fonts/raleway/,
                UprightFont=*-ExtraLight,
                BoldFont=*-Bold,           # Adjust this if you want another variant as the bold sans-serif
                ItalicFont=*-ExtraLightIt, # If there's an italic version of ExtraLight; adjust if needed
                BoldItalicFont=*-BoldIt    # Adjust this if you want another variant as the bold italic sans-serif
            ]{Raleway}
            """
        )
    )
    doc.append(
        NoEscape(
            r"\newcommand{\custombold}[1]{\color{subheadings}\fontspec[Path = ./fonts/lato/]{Lato-Bol}\selectfont #1 \normalfont}"
        )
    )

    # Date
    doc.append(NoEscape(r"\setlength{\TPHorizModule}{1mm}"))
    doc.append(NoEscape(r"\setlength{\TPVertModule}{1mm}"))
    doc.append(NoEscape(r"\textblockorigin{0mm}{5mm}"))
    doc.append(NoEscape(r"\newcommand{\lastupdated}{\begin{textblock}{60}(165,0)"))
    doc.append(
        NoEscape(
            r"\color{date}\fontspec[Path = fonts/raleway/]{Raleway-ExtraLight}\fontsize{8pt}{10pt}\selectfont"
        )
    )
    doc.append(NoEscape(r"Last Updated on"))
    doc.append(NoEscape(r"\today"))
    doc.append(NoEscape(r"\end{textblock}}"))

    # Name section
    doc.append(
        NoEscape(
            r"""
            \newcommand{\namesection}[3]{
                \vspace{-10pt}
                \raggedright{
                    \fontspec[Path = fonts/lato/]{Lato-Lig}
                    \fontsize{40pt}{10cm}\selectfont #1 
                    \selectfont #2
                } \\
                \vspace{-10pt}
                \raggedright{ 
                    \color{headings}
                    \fontspec[Path = fonts/raleway/]{Raleway-Medium}
                    \fontsize{11pt}{14pt}
                    \selectfont #3
                }
            }
            """
        )
    )

    # Headings
    doc.append(NoEscape(r"\titlespacing{\section}{0pt}{0pt}{0pt}"))
    doc.append(
        NoEscape(
            r"""
            \titleformat{\section}{\color{headings}
            \scshape\fontspec[Path = fonts/lato/]{Lato-Lig}\fontsize{16pt}{24pt}\selectfont \raggedright\uppercase}{} {0em}{}
            """
        )
    )

    # Subheadings
    doc.append(
        NoEscape(
            r"""
            \titleformat{\subsection}{\color{subheadings}
            \fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{12pt}{12pt}\selectfont\bfseries\uppercase}{}{0em}{}
            """
        )
    )
    doc.append(NoEscape(r"\titlespacing{\subsection}{0pt}{\parskip}{-\parskip}"))
    doc.append(NoEscape(r"\titlespacing{\subsubsection}{0pt}{\parskip}{-\parskip}"))
    doc.append(
        NoEscape(
            r"""
            \newcommand{\runsubsection}[1]{\color{subheadings}
            \fontspec[Path = fonts/lato/]{Lato-Bol}\fontsize{12pt}{12pt}\selectfont\bfseries\uppercase {#1} \normalfont}
            """
        )
    )

    # Descriptors
    doc.append(
        NoEscape(
            r"""
            \newcommand{\descript}[1]{\color{subheadings}\raggedright\scshape\fontspec[Path = fonts/raleway/]{Raleway-Medium}\fontsize{11pt}{13pt}\selectfont {#1 \\} \normalfont}
            """
        )
    )

    # Location
    doc.append(
        NoEscape(
            r"""
            \newcommand{\location}[1]{\color{headings}\raggedright\fontspec[Path = fonts/raleway/]{Raleway-Regular}\fontsize{10pt}{12pt}\selectfont {#1\\} \normalfont}
            """
        )
    )
    doc.append(
        NoEscape(
            r"""
            \newcommand{\locationtitle}[1]{\color{headings}\raggedright\fontspec[Path = fonts/raleway/]{Raleway-Bold}\fontsize{10pt}{12pt}\selectfont {#1\\} \normalfont}
            """
        )
    )

    # Section separators and bullet lists
    doc.append(NoEscape(r"\newcommand{\sectionsep}[0]{\vspace{8pt}}"))
    doc.append(NoEscape(r"\setlength{\columnsep}{1cm}"))
    doc.append(
        NoEscape(
            r"\newenvironment{tightemize}{\vspace{-\topsep}\begin{itemize}\itemsep1pt \parskip0pt \parsep0pt}{\end{itemize}\vspace{-\topsep}}"
        )
    )
    doc.append(NoEscape(r"\newcommand{\customrowheight}{\vspace{0.1cm}}"))

    # Start of the content
    with doc.create(MiniPage(width=r"0.55\textwidth", align="t")):
        # Name section
        doc.append(
            NoEscape(
                r"\namesection{\custombold{Adrian Darian}}{}{\urlstyle{same}\url{} \\ \href{mailto:adarian@ucmerced.edu}{adarian@ucmerced.edu} | 858.472.9530} \\"
            )
        )

        # Experience
        with doc.create(Section(NoEscape(r"\custombold{Experience}"), numbering=False)):
            # Roche Tissue Diagnostics
            doc.append(NoEscape(r"\runsubsection{Roche Tissue Diagnostics}"))
            doc.append(NoEscape(r"\descript{| Software Imaging Intern}"))
            doc.append(NoEscape(r"\location{May 2019 – August 2019 | Santa Clara, CA}"))
            with doc.create(Tightemize()):
                doc.append(
                    NoEscape(
                        r"\item Developed and deployed several web applications for digital pathology; built in \custombold{Angular 8} with the \custombold{Redux pattern}."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Configured a network of \custombold{logging solutions and performance monitors} for various applications and micro services, as well as multiple servers using ELK Stack; \custombold{Elasticsearch, Logstash and Kibana}."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Worked in an \custombold{Agile} environment using the \custombold{SCRUM} methodologies to collaborate with imaging scientists, pathologists, and software engineers to build a whole slide image viewer and a detailed monitoring system."
                    )
                )

            # CatCard
            doc.append(NoEscape(r"\runsubsection{CatCard}"))
            doc.append(NoEscape(r"\descript{| Full Stack Developer}"))
            doc.append(NoEscape(r"\location{May 2018 – Present | Merced, CA}"))
            with doc.create(Tightemize()):
                doc.append(
                    NoEscape(
                        r"\item Implementing scalable and shared \custombold{build, test and deployment} automation systems."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Designed an intuitive layout with \custombold{Vue.js} and \custombold{Node.js} for \custombold{realtime data visualization} of events, vendors, facilities and departments with \custombold{MapBox}."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Optimized the \custombold{compile time} from \custombold{20 seconds to 4 seconds} for all services."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Improved the \custombold{run time} for the departments main application from \custombold{5 minutes to 3 minutes}."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Converting \custombold{synchronous PHP} to \custombold{asynchronous Node.js}."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Increased \custombold{user retention} by \custombold{23\%}, by enhancing the user\'s experience and expanding the functionality of the organization\'s applications."
                    )
                )

            # HackMerced
            doc.append(NoEscape(r"\runsubsection{HackMerced}"))
            doc.append(NoEscape(r"\descript{| Executive Director}"))
            doc.append(NoEscape(r"\location{March 2017 – Present | Merced, CA}"))
            with doc.create(Tightemize()):
                doc.append(
                    NoEscape(
                        r"\item Constructed HackMerced\'s official websites from scratch using primarily \custombold{React.js}: \custombold{HackMerced, HackMerced V, HackMerced IV and HackMerced III}."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Deployed custom \custombold{DigitalOcean droplets} to house all HackMerced related applications, multiple \custombold{Heroku pipelines}, and image hosting with \custombold{AWS S3} buckets with build tests through \custombold{CircleCI}."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Hosted \custombold{600 participants} from around the world and facilitated \custombold{30+} project submissions."
                    )
                )

            # Ozone
            doc.append(NoEscape(r"\runsubsection{Ozone}"))
            doc.append(NoEscape(r"\descript{| Software Engineer}"))
            doc.append(
                NoEscape(r"\location{January 2018 - February 2019 | Merced, CA}")
            )
            with doc.create(Tightemize()):
                doc.append(
                    NoEscape(
                        r"\item Visualized \custombold{2,000+ data sets} from facilities databases using \custombold{Mapbox} and \custombold{D3.js}."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Deployed a \custombold{Progressive Web Application} on \custombold{DigitalOcean} with the \custombold{MySQL, Express, React.js, Node.js} Stack."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Established a sustainability awareness platform used by \custombold{1,000+} students and \custombold{4} departments at UC Merced."
                    )
                )

            # MACES, NASA
            doc.append(NoEscape(r"\runsubsection{MACES, NASA}"))
            doc.append(NoEscape(r"\descript{| Web Developer}"))
            doc.append(
                NoEscape(r"\location{December 2016 – February 2018 | Merced, CA}")
            )
            with doc.create(Tightemize()):
                doc.append(
                    NoEscape(
                        r"\item Designed MACES main site, the director\'s personal site and the stem resource center\'s site with a custom \custombold{jQuery} and \custombold{JSON CMS}."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Studied, reevaluated, and reformed the \custombold{User Interface} and \custombold{User Experience} for all sites."
                    )
                )
                doc.append(
                    NoEscape(
                        r"\item Increased site activity by \custombold{72\%} by expanding upon the site\'s functionality."
                    )
                )    
    
    doc.append(NoEscape(r"\hspace{0.2cm}"))


    # Start of the second column
    with doc.create(MiniPage(width=r"0.38\textwidth", align="t")):
        # Links
        doc.append(
            NoEscape(
                r"GitHub: \href{https://github.com/adriandarian}{\custombold{/adriandarian}} \\"
            )
        )
        doc.append(
            NoEscape(
                r"LinkedIn: \href{https://www.linkedin.com/in/adriandarian}{\custombold{/in/adriandarian}} \\"
            )
        )
        doc.append(
            NoEscape(
                r"Devpost: \href{https://www.devpost.com/adarian}{\custombold{/adarian}} \\"
            )
        )
        doc.append(
            NoEscape(
                r"StackOverflow: \href{https://stackoverflow.com/users/9647369/adarian}{\custombold{/users/9647369/adarian}} \\"
            )
        )

        # Education
        with doc.create(Section(NoEscape(r"\custombold{Education}"), numbering=False)):
            doc.append(NoEscape(r"\locationtitle{University of California, Merced}"))
            doc.append(
                NoEscape(
                    r"\location{Bachelor of Science in Computer Science and Engineering}"
                )
            )

        # Coursework
        with doc.create(Section(NoEscape(r"\custombold{Coursework}"), numbering=False)):
            doc.append(NoEscape(r"Algorithm Design and Analysis \\"))
            doc.append(NoEscape(r"Computer Graphics \\"))
            doc.append(NoEscape(r"Database Systems and Implementations \\"))
            doc.append(NoEscape(r"Object Oriented Programming \\"))
            doc.append(NoEscape(r"Operating Systems \\"))
            doc.append(NoEscape(r"Robotic Operating Systems (ROS) \\"))
            doc.append(NoEscape(r"Spatial Analysis \\"))

        # Skills
        with doc.create(Section(NoEscape(r"\custombold{Skills}"), numbering=False)):
            doc.append(NoEscape(r"\location{\custombold{Languages:}}"))
            doc.append(
                NoEscape(r"JavaScript \textbullet{} TypeScript \textbullet{} Python \\")
            )
            doc.append(
                NoEscape(
                    r"C/C++ \textbullet{} PHP \textbullet{} Java \textbullet{} C\# \textbullet{} Go \\"
                )
            )

            doc.append(NoEscape(r"\location{\custombold{Frameworks:}}"))
            doc.append(
                NoEscape(r"Angular \textbullet{} React.js \textbullet{} Node.js \\")
            )
            doc.append(
                NoEscape(r"Vue.js \textbullet{} Flutter \textbullet{} Django \\")
            )

            doc.append(NoEscape(r"\location{\custombold{Databases:}}"))
            doc.append(
                NoEscape(r"MySQL \textbullet{} MongoDB \textbullet{} OracleDB \\")
            )
            doc.append(
                NoEscape(r"Firebase \textbullet{} PostgreSQL \textbullet{} DynamoDB \\")
            )

            doc.append(NoEscape(r"\location{\custombold{Services:}}"))
            doc.append(NoEscape(r"DigitalOcean \textbullet{} AWS \textbullet{} GCP \\"))
            doc.append(NoEscape(r"ELK \textbullet{} ArcGIS \textbullet{} Unity"))

        # Awards
        with doc.create(Section(NoEscape(r"\custombold{Awards}"), numbering=False)):
            with doc.create(Tabular("ll")) as table:
                table.add_row(("Impact Awards 2019", "Campus Technology"))
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(("UC Merced 2019", "Innovation Award"))
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(("DPHackathon 2019", NoEscape(r"3$^{rd}$ Place")))
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(("UC Merced 2019", "Program of the Year"))
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(("NACCU 2019", "Innovative Technology Award"))
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(("SLO Hacks 2019", "Best GCP Hacks"))
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(("ValleyHacks 2019", NoEscape(r"1$^{st}$ Place")))
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(
                    (
                        "SacHacks 2019",
                        NoEscape(r"\parbox{5cm}{2$^{nd}$ Place \\ Best DigitalOcean Hack}"),
                    )
                )
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(
                    ("SDHacks 2018", NoEscape(r"\parbox{5cm}{3$^{rd}$ Place \\ DoD Track SPAWAR}"))
                )
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(("CITRIS MAC", "$2,000 Finalist Prize"))
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(("Innovate to Grow", "Finals Qualifier"))
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(("Hack Fresno 2018", "Best Hardware Hack"))
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(
                    (
                        "Citrus Hacks 2018",
                        NoEscape(r"\parbox{5cm}{3$^{rd}$ Place \\ \$1,000 Entrepreneurship}")
                    )
                )
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(("HackDavis 2018", "Best Environmental Hack"))
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(("HackMerced 2017", "Best In Design"))
                table.append(NoEscape(r"\customrowheight"))
                table.add_row(("BSA", "Eagle Scout"))

    # Generate the document
    doc.generate_pdf("resume", clean_tex=False, compiler="xelatex")
