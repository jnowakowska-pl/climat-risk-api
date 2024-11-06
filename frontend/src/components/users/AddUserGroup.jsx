import React, { useState, useEffect } from 'react';

const AddUserGroup = () => {
  const [groupName, setGroupName] = useState('');
  const [groupDescription, setGroupDescription] = useState('');
  const [permissions, setPermissions] = useState([]);
  const [selectedPermission, setSelectedPermission] = useState('');

    // Fetch permissions from the API
    const fetchPermissions = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/core/permissions/');
        const data = await response.json();
        setPermissions(data);
      } catch (error) {
        console.error('Error fetching permissions:', error);
      }
    };

    useEffect(() => {
      fetchPermissions();
    }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = {
      group_name: groupName,
      group_description: groupDescription,
      permission: selectedPermission,
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/api/core/usergroups/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        alert('User group added successfully!');
        setGroupName('');
        setGroupDescription('');
        setSelectedPermission('');
      } else {
        alert('Failed to add user group.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while adding the user group.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="groupName">Group Name:</label>
        <input
          type="text"
          id="groupName"
          value={groupName}
          onChange={(e) => setGroupName(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="groupDescription">Group Description:</label>
        <textarea
          id="groupDescription"
          value={groupDescription}
          onChange={(e) => setGroupDescription(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="permission">Permission:</label>
        <select
          id="permission"
          value={selectedPermission}
          onChange={(e) => setSelectedPermission(e.target.value)}
          onClick={fetchPermissions} // Fetch permissions on dropdown click
          required
        >
          <option value="">Select a permission</option>
          {permissions.map((permission) => (
            <option key={permission.permission_id} value={permission.permission_id}>
              {permission.permission_name}
            </option>
          ))}
        </select>
      </div>
      <button type="submit">Add User Group</button>
    </form>
  );
};

export default AddUserGroup