import React from 'react';
import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import SetUserPermissionsDialog from './SetUserPermissionsDialog';

export default function Admin() {

  const [anchorEl, setAnchorEl] = React.useState(null);

  const handleClick = event => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <div>
      <Button
        aria-controls="simple-menu"
        aria-haspopup="true"
        onClick={handleClick}
        color="inherit"
    >
        Admin
      </Button>
      <Menu
        id="simple-menu"
        anchorEl={anchorEl}
        keepMounted
        open={Boolean(anchorEl)}
        onClose={handleClose}
      >
        <SetUserPermissionsDialog>
            <MenuItem onClick={handleClose}>Set User Permissions</MenuItem>
        </SetUserPermissionsDialog>
        <MenuItem onClick={handleClose}>Close</MenuItem>
      </Menu>
    </div>
  );
}