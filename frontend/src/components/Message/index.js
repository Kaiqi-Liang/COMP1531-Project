import React from 'react';
import timeago from 'epoch-timeago';
import axios from 'axios';

import {
  Avatar,
  ListItem,
  ListItemIcon,
  ListItemText,
} from '@material-ui/core';


import AuthContext from '../../AuthContext';
import MessagePin from './MessagePin';
import MessageReact from './MessageReact';
import MessageRemove from './MessageRemove';
import MessageEdit from './MessageEdit';


function Message({
  message_id,
  message = '',
  u_id,
  time_created,
  is_unread = false,
  is_pinned = false,
  reacts = [] /* [{ react_id, u_ids }] */,
}) {

  const [name, setName] = React.useState();
  const [initials, setInitials] = React.useState();
  const [imgUrl, setImgUrl] = React.useState();
  const token = React.useContext(AuthContext);
  React.useEffect(() => {
    setName();
    setInitials();
    setImgUrl()
    axios
      .get(`/user/profile`, {
        params: {
          token,
          u_id,
        },
      })
      .then(({ data }) => {
        const {
          email = '',
          name_first = '',
          name_last = '',
          handle_str = '',
          profile_img_url = '',
        } = data;
        setName(`${name_first} ${name_last}`);
        setInitials(`${name_first[0]}${name_last[0]}`);
        setImgUrl(`${profile_img_url}`)
      })
      .catch((err) => {
        console.error(err);
      });
  }, [message_id, token, u_id]);

  return (
    <ListItem key={message_id} style={{ width: '100%' }}>
      {name && initials && message && (
        <>
          <ListItemIcon>
            <img className="avatar-small" src={imgUrl} />
          </ListItemIcon>
          <div
            style={{
              display: 'flex',
              width: '100%',
              justifyContent: 'space-between',
              alignItems: 'center',
            }}
          >
            <ListItemText
              primary={
                <>
                  <span>{name}</span>
                  <span style={{ paddingLeft: 10, fontSize: 10 }}>
                    {timeago(time_created * 1000)}
                  </span>
                </>
              }
              secondary={message}
            />
            <div style={{ display: 'flex', height: 30, marginLeft: 20 }}>
              <MessageReact
                message_id={message_id}
                reacts={reacts}
                u_id={u_id}
              />
              <MessagePin
                message_id={message_id}
                is_pinned={is_pinned}
              />
              <MessageEdit
                message_id={message_id}
              />
              <MessageRemove
                message_id={message_id}
              />
            </div>
          </div>
        </>
      )}
    </ListItem>
  );
}

export default Message;
