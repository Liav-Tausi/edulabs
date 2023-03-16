import { AppBar, MenuItem, Toolbar } from "@mui/material";
import { Box } from "@mui/system";
import { NavLink, Outlet, useLocation } from "react-router-dom";
import "./Layout.css";



export default function Layout() {
  const currLocation = useLocation();
  console.log("Layout:", currLocation);

  let activeStyle = {
    textDecoration: "underline",
  };

  return (
    <Box>
      <AppBar position="static">
        <Toolbar variant="dense">
          <MenuItem>
            <NavLink
              to="/"
              className="nav-link"
              style={({ isActive }) => (isActive ? activeStyle : undefined)}
            >
              Home
            </NavLink>
          </MenuItem>
          <MenuItem>
            <NavLink
              to="countries/"
              className="nav-link"
              style={({ isActive }) => (isActive ? activeStyle : undefined)}
            >
              Countries
            </NavLink>
          </MenuItem>

          <MenuItem>
            <NavLink
              to="countdown/"
              className="nav-link"
              style={({ isActive }) => (isActive ? activeStyle : undefined)}
            >
              Countdown
            </NavLink>
          </MenuItem>
          <MenuItem>
            <NavLink
              to="showip/"
              className="nav-link"
              style={({ isActive }) => (isActive ? activeStyle : undefined)}
            >
              ShowIp
            </NavLink>
          </MenuItem>
          <MenuItem>
            <NavLink
              to="colorcomp/"
              className="nav-link"
              style={({ isActive }) => (isActive ? activeStyle : undefined)}
            >
              ColorComp
            </NavLink>
          </MenuItem>
        </Toolbar>
      </AppBar>

      <Outlet />
    </Box>
  );

  // function HeaderMenuItem(props) {
  //     const location = useLocation()

  //     console.log(props)
  //     console.log('location',location)

  //     let activeStyle = {
  //         textDecoration: "underline",
  //       };

  //     let currClass = 'nav-link '
  //     if (location.pathname.includes(props.name)) {
  //         currClass += 'active-nav-link'
  //     }

  //     console.log('setting class',props.name, currClass)

  //     return (
  //         <MenuItem>
  //         <NavLink to='/' className={currClass}>
  //             {props.children}
  //         </NavLink>
  //     </MenuItem>
  //     )
  // }

  // return(
  //     <Box>
  //         <AppBar position="static">
  //             <Toolbar variant="dense">
  //             {/* <MenuItem>
  //                 <NavLink to='/' className='nav-link'
  //                 style={({ isActive }) =>
  //                 isActive ? activeStyle : undefined
  //               }>
  //                     Home
  //                 </NavLink>
  //             </MenuItem> */}
  //             <HeaderMenuItem name='home'>
  //                 Home
  //             </HeaderMenuItem>
  //             <HeaderMenuItem name='countries'>
  //                 Countries
  //             </HeaderMenuItem>
  //             {/* <MenuItem>
  //                 <NavLink to='countries/'
  //                         className='nav-link'
  //                         style={({ isActive }) =>
  //                 isActive ? activeStyle : undefined
  //               }>
  //                     Countries
  //                 </NavLink>
  //             </MenuItem> */}
  //             </Toolbar>
  //         </AppBar>

  //         <Outlet />
  //     </Box>
  // )
}
