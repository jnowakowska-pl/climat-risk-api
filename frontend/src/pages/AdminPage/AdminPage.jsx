import React from "react";
import './AdminPage.css';
import AddPermissions from '../../components/permissions/AddPermissions';
import AddUserGroup from '../../components/users/AddUserGroup';

function AdminPage() {
  return (
    <div className="container">
    <AddPermissions />
<AddUserGroup />
    </div>
  );
}

export default AdminPage;