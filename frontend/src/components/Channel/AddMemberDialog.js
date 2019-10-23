import React from 'react';
import axios from 'axios';

import {
  Dialog,
  DialogTitle,
  DialogActions,
  DialogContent,
  DialogContentText,
  Button,
  TextField,
} from '@material-ui/core';
import AuthContext from '../../AuthContext';
import { toast } from 'react-toastify';
import { DEFAULT_ERROR_TEXT } from '../../utils/text';

function AddMemberDialog({ channel_id, ...props }) {
  const [open, setOpen] = React.useState(false);
  const token = React.useContext(AuthContext);
  function handleClickOpen() {
    setOpen(true);
  }
  function handleClose() {
    setOpen(false);
  }
  function handleSubmit(event) {
    event.preventDefault();
    const user_id = event.target[0].value;

    if (!user_id) return;

    axios.post(`/channel/invite`, { token, user_id, channel_id })
      .then((response) => {
        console.log(response);
      })
      .catch((err) => {
        console.error(err);
        toast.error(DEFAULT_ERROR_TEXT);
      });
  }
  return (
    <div>
      <Button variant="outlined" color="primary" onClick={handleClickOpen}>
        Invite Member
      </Button>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="form-dialog-title"
      >
        <DialogTitle id="form-dialog-title">Invite User</DialogTitle>
        <form onSubmit={handleSubmit}>
          <DialogContent>
            <DialogContentText>
              Enter a user id below to invite a user to this channel
            </DialogContentText>
            <TextField
              autoFocus
              margin="dense"
              id="user_id"
              label="User ID"
              name="user_id"
              fullWidth
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={handleClose} color="primary">
              Cancel
            </Button>
            <Button onClick={handleClose} type="submit" color="primary">
              Invite
            </Button>
          </DialogActions>
        </form>
      </Dialog>
    </div>
  );
}

export default AddMemberDialog;
