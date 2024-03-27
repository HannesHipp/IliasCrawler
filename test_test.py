html_doc = """
<li data-jstree='{ "disabled" : true  }' id="exp_node_lm_exp_458787" rel="disabled">
    <a href="ilias.php?ref_id=2147595&amp;obj_id=458787&amp;cmd=layout&amp;cmdClass=illmpresentationgui&amp;cmdNode=go&amp;baseClass=ilLMPresentationGUI">
        <img src="./templates/default/images/icon_st.svg"/>
        <span class="loader">
        </span>
        <span class="ilExp2NodeContent">
        Kapitel 1
        </span>
    </a>
    <ul>
        <li data-jstree='{ "disabled" : true  }' id="exp_node_lm_exp_458791" rel="disabled">
            <a href="ilias.php?ref_id=2147595&amp;obj_id=458791&amp;cmd=layout&amp;cmdClass=illmpresentationgui&amp;cmdNode=go&amp;baseClass=ilLMPresentationGUI">
                <img src="./templates/default/images/icon_st.svg"/>
                <span class="loader">
                </span>
                <span class="ilExp2NodeContent">
                Kapitel 1.1
                </span>
            </a>
        </li>
        <li data-jstree='{ "disabled" : true  }' id="exp_node_lm_exp_460732" rel="disabled">
            <a href="ilias.php?ref_id=2147595&amp;obj_id=460732&amp;cmd=layout&amp;cmdClass=illmpresentationgui&amp;cmdNode=go&amp;baseClass=ilLMPresentationGUI">
                <img src="./templates/default/images/icon_st.svg"/>
                <span class="loader">
                </span>
                <span class="ilExp2NodeContent">
                Kapitel 1.2
                </span>
            </a>
        </li>
    </ul>
</li>
"""



from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')
soup = soup.find_all('li')[0]
print(soup.prettify())
print("")
tags = soup.find_all('li')
for tag in tags:
    print(soup == tag)