import React, { useState } from "react";
import './LandingPage.css';
import AddPermissions from '../../components/permissions/AddPermissions';
import AddUserGroup from '../../components/users/AddUserGroup';
import Map from '../../components/mapComponents/MapItem/MapItem';
import SideBar from "../../components/mapComponents/SideBar/SideBar";
import UserProfile from "../../components/mapComponents/UserProfile/UserProfile";
import SearchInput from "../../components/mapComponents/SearchInput/SearchInput";
import MapZoom from "../../components/mapComponents/mapZoom/mapZoom";
import InfoBillboard from "../../components/mapComponents/InfoBillboard/InfoBillboard";
import Legend from "../../components/mapComponents/Legend/Legend";
import LowerPanel from "../../components/mapComponents/LowerPanel/LowerPanel";
import HigherPanel from "../../components/mapComponents/HigherPanel/HigherPanel";

function LandingPage() {

  const [mapZoom, setMapZoom] = useState(6)

  return (
    <div id="landingPage">
      <Map mapZoom={mapZoom} />
      <MapZoom mapZoom={mapZoom} setMapZoom={setMapZoom} />
      <SideBar/>
      <UserProfile/>
      <SearchInput/>
      <InfoBillboard />
      <Legend />
      <LowerPanel />
      <HigherPanel />
    </div>
  );
}

export default LandingPage;