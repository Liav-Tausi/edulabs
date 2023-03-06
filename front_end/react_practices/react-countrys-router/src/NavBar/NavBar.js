import { AppBar, List, ListItem, Toolbar } from "@mui/material";

import { Outlet, NavLink } from "react-router-dom";

const NavBar = () => {
  return (
    <>
      <AppBar sx={{ position: "sticky" }}>
        <Toolbar sx={{ justifyContent: "center" }}>
          <List sx={{ columns: 3 }}>
            <ListItem sx={{ justifyContent: "center" }}>
              <NavLink
                to="joke"
                style={{ color: "white", textDecoration: "none"}}
              >
                Jokes
              </NavLink>
            </ListItem>
            <ListItem>
              <NavLink
                to="country"
                style={{ color: "white", textDecoration: "none" }}
              >
                Countries
              </NavLink>
            </ListItem>
            <ListItem sx={{ justifyContent: "center" }}>
              <NavLink
                to="about"
                style={{ color: "white", textDecoration: "none" }}
              >
                About
              </NavLink>
            </ListItem>
          </List>
        </Toolbar>
      </AppBar>
      <Outlet />
    </>
  );
};

export default NavBar;
