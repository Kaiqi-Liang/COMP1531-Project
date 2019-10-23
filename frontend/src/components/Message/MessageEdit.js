import React from 'react';
import axios from 'axios';

import {
    IconButton,
} from '@material-ui/core';

import EditIcon from '@material-ui/icons/Edit';

import AuthContext from '../../AuthContext';

function MessageEdit({
    message_id,
}) {

    const token = React.useContext(AuthContext);

    const messageEdit = () => {
        const message = prompt();
        if (!message) return; // basic validation
        axios.post(`/message/edit`, {
            token,
            message_id,
            message,
        });
    };

    return (
        <IconButton
            onClick={messageEdit}
            style={{ margin: 1 }}
            size="small"
            edge="end"
            aria-label="delete"
        >
            <EditIcon fontSize="small" />
        </IconButton>
    );
}

export default MessageEdit;
