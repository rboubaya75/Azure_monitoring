//import useState hook to create menu collapse state
import React, { useState, useEffect } from "react";
import axios from 'axios'

//import react pro sidebar components
import {
  ProSidebar,
  Menu,
  MenuItem,
  SidebarHeader,
  SidebarFooter,
  SidebarContent,
} from "react-pro-sidebar";

//import sidebar css from react-pro-sidebar module and our custom css 
import "react-pro-sidebar/dist/css/styles.css";
import "./Sidebar.css";

const Sidebar= (props) => {
  
  //create initial menuCollapse state using useState hook
  const [menuCollapse, setMenuCollapse] = useState(false)

  const [items, setItems] = useState([])

  useEffect(async() => {
    const getItems = async() => {
      const res = await axios(`https://brtazuremonitor.azurewebsites.net/api/${props.page}`)
      setItems(res.data.map(e => e.name));
    }
    getItems()
  }, [])
  return (
    <>
      <div id="header">
          {/* collapsed props to change menu size using menucollapse state */}
        <ProSidebar collapsed={menuCollapse}>
          <SidebarHeader>
          </SidebarHeader>
          <SidebarContent>
            <Menu iconShape="square">
              {items.map(item => <MenuItem key={item}>{item}</MenuItem>)}
            </Menu>
          </SidebarContent>
          <SidebarFooter>
          </SidebarFooter>
        </ProSidebar>
      </div>
    </>
  );
};

export default Sidebar;
