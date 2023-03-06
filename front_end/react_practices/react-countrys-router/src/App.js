import "./App.css";
import NavBar from "./NavBar/NavBar";
import { Routes, Route } from "react-router-dom";
import ChuckNoris from "./ChuckNoris/ChuckNoris";
import Countries from "./Countries/Countries";
import About from "./About/About";
import Welcome from "./welcome/welcome";
import NoMatch from "./NoMatch/NoMatch";
import Country from "./Country/Country";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<NavBar />}>
        <Route index element={<Welcome />} />
        <Route path="joke" element={<ChuckNoris />} />
        <Route path="country" element={<Countries />} />
        <Route path="about" element={<About />} />
        <Route path="/country/:countryId" element={<Country />} />

        <Route path="*" element={<NoMatch />} />
      </Route>
    </Routes>
  );
};

export default App;
