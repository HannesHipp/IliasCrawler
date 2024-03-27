from IliasCrawler.Session import Session


Session.set_session('st162876', '90.0kg@Sommer')

soup = Session.get_content('https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems')
pretty_html = soup.prettify()
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(pretty_html)