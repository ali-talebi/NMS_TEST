from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest  
import time 




@pytest.mark.zonemanagement_zonename_select 
def tfu_zonemanagement_zonename_select( set_up_test ) : 
    login_web_nms = set_up_test 
    def wait_for_element_clickable( element , timeout  ) : 
        for i in range(timeout * 4 ) :
            try : 
                if element.is_enabled() : 
                    return element 
            except : 
                time.sleep(0.3)
                continue 
        else : 
            return False 

    time.sleep(0.5) 
    login_web_nms.find_element(By.XPATH , '//*[@data-testid ="discovery"]').click() 
    time.sleep(1) 
    login_web_nms.find_element(By.XPATH , '//div[@data-testid="zones-list-filter-icon"]').click() 
    time.sleep(1.5) 
    login_web_nms.find_element(By.XPATH , '//input[@data-testid ="zone-name-filter" ]').click() 
    time.sleep(1.5)
    total_drop_zone = login_web_nms.find_elements(By.XPATH , '//div[@class="shakil-select-options-item"]')
    time.sleep(3)
    total_zone_name = [ i.text for i in total_drop_zone ]
    time.sleep(3)

    
    print("names of Zone  " , total_zone_name )
    time.sleep(3)
    selected_name = []
    for option in total_drop_zone  :
        try :  
            return_element = wait_for_element_clickable(option , 10 )
            if return_element != None : 
                option.click()    
                selected_name.append(option.text)

            time.sleep(3)
        except : 
            continue 
    

    total_row_selected = login_web_nms.find_elements(By.XPATH , '//table/tbody/tr/td[2]/div')
    total_row_return = []
    for item in total_row_selected : 
        total_row_return.append(item.text)

    print("Total Returned of Row : " , total_row_return )
    for zone in selected_name : 
        assert zone not in total_row_return 


@pytest.mark.nodemanagement_nodename_select 
def tfu_nodemanagement(set_up_test) : 
    login_web_nms = set_up_test
    login_web_nms.maximize_window()
    time.sleep(3)
    login_web_nms.find_element(By.XPATH , '//*[@data-testid ="discovery"]').click() 
    time.sleep(3)
    login_web_nms.find_element(By.XPATH , '//div[@data-testid = "node-management"]').click()
    time.sleep(3)
    login_web_nms.find_element(By.XPATH , '//div[@data-testid = "nodes-list-filter-icon" ]').click()
    time.sleep(3)
    login_web_nms.find_element(By.XPATH , '//input[@data-testid = "node-name-filter" ]').click() 
    total_drop_node = login_web_nms.find_elements(By.XPATH , '//div[@class="shakil-select-options-item"]')
    
    
    print("Total Drop Element : " , len(total_drop_node))
    time.sleep(3)
    total_node_name = [ i.text for i in total_drop_node ]
    time.sleep(3)
    if len(total_drop_node) >= 1 : 
        counter = None 
        if len(total_drop_node) == 1 : 
            counter = 0 
        elif len(total_drop_node) > 1 : 
            counter = -1 
        
        print("names : " , total_node_name )
        time.sleep(3)
        selected_name = []
        for option in total_drop_node  :
            try :  
                selected_name.append(option.text)
                option.click()
                time.sleep(3)
            except : 
                continue 

        total_row_selected = login_web_nms.find_elements(By.XPATH , '//table/tbody/tr/td[2]/div')
        total_row_return = []
        for item in total_row_selected : 
            total_row_return.append(item.text)

        print("Total Returned of Row : " , total_row_return )
        for node in selected_name : 
            assert node not in total_row_return 
        
