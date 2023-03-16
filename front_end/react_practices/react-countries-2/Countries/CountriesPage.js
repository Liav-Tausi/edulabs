import { List, ListItem, ListItemButton } from "@mui/material";
import { Box } from "@mui/system";
import { Link, Outlet, useLocation } from "react-router-dom";

export default function CountriesPage() {

    const currLocation = useLocation()
    console.log('location', currLocation)

    return(
        <Box>
            <h1>Countries List:</h1>

            <ul>
                <li>
                    <Link to='israel/'>Israel</Link>
                </li>
                <li>
                    <Link to='france/'>France</Link>
                </li>
                <li>
                    <Link to='germany/'>Germany</Link>
                </li>
                <li>
                    <Link to='?country=belgium'>Belgium</Link>
                </li>
            </ul>

            <hr />

            <Outlet />
        </Box>
    )
}