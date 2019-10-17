import React from 'react';
import axios from 'axios';

import { IconButton } from '@material-ui/core';

import DeleteIcon from '@material-ui/icons/Delete';

import { url } from '../../utils/constants';

import AuthContext from '../../AuthContext';

function MessageRemove({
  message_id,
}) {

  const token = React.useContext(AuthContext);

  const messageRemove = () => {
    axios.post(`${url}/message/remove`, {
      token,
      message_id,
    });
  };


  return (
    <IconButton
      onClick={messageRemove}
      style={{ margin: 1 }}
      size="small"
      edge="end"
      aria-label="delete"
    >
      <DeleteIcon fontSize="small" />
    </IconButton>
  );
}

export default MessageRemove;
