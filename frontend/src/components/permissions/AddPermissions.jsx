// src/AddPermissions.js
import React, { useState } from 'react';
import './AddPermissions.css';

const AddPermissions = () => {
  const [permissionName, setPermissionName] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = {
      permission_name: permissionName,
      description: description,
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/api/core/permissions/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        alert('Permission added successfully!');
        setPermissionName('');
        setDescription('');
      } else {
        alert('Failed to add permission.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while adding the permission.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="permissionName">Permission Name:</label>
        <input
          type="text"
          id="permissionName"
          value={permissionName}
          onChange={(e) => setPermissionName(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="description">Description:</label>
        <textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <button type="submit">Add Permission</button>
    </form>
  );
};

export default AddPermissions;