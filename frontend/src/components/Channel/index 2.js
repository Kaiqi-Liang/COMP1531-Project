import {
  Avatar,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  ListSubheader,
  Typography,
  Button,
  Grid,
  Link,
  IconButton,
} from '@material-ui/core';
import PersonAdd from '@material-ui/icons/PersonAdd';
import PersonAddDisabled from '@material-ui/icons/PersonAddDisabled';
import axios from 'axios';
import React from 'react';
import { toast } from 'react-toastify';
import { url } from '../../utils/constants';
import { CHANNEL_ERROR_TEXT, DEFAULT_ERROR_TEXT } from '../../utils/text';
import AddMemberDialog from './AddMemberDialog';
import ChannelMessages from './ChannelMessages';
import AuthContext from '../../AuthContext';
import { extractUId } from '../../utils/token';

function Channel({ channel_id, ...props }) {
  const [name, setName] = React.useState('');
  const [members, setMembers] = React.useState([]);
  const [owners, setOwners] = React.useState([]);
  const token = React.useContext(AuthContext);
  const u_id = extractUId(token);

  function fetchChannelData(channel_id, token) {
    axios
      .get(`${url}/channel/details`, {
        params: {
          token,
          channel_id,
        },
      })
      .then(({ data }) => {
        console.log(data);
        const { name, owner_members, all_members } = data;
        // assumes members of form [{ u_id, name_first, name_last }]
        setMembers(all_members);
        setOwners(owner_members);
        setName(name);
      })
      .catch((err) => {
        console.error(err);
        toast.error(CHANNEL_ERROR_TEXT);
      });
  }
  React.useEffect(() => {
    fetchChannelData(channel_id, token);
  }, [channel_id, token]);

  function joinChannel(channel_id, token) {
    axios
      .post(`${url}/channel/join`, {
        token,
        channel_id,
      })
      .then(() => {
        fetchChannelData(channel_id, token);
      })
      .catch((err) => {
        console.error(err);
        toast.error(DEFAULT_ERROR_TEXT);
      });
  }

  function leaveChannel(channel_id, token) {
    axios
      .post(`${url}/channel/leave`, {
        token,
        channel_id,
      })
      .then(() => {
        fetchChannelData(channel_id, token);
      })
      .catch((err) => {
        console.error(err);
        toast.error(DEFAULT_ERROR_TEXT);
      });
  }

  function addOwner(u_id) {
    axios
      .post(`${url}/channel/addowner`, {
        token,
        channel_id,
        u_id,
      })
      .then(() => {
        fetchChannelData(channel_id, token);
      })
      .catch((err) => {
        console.error(err);
        toast.error(DEFAULT_ERROR_TEXT);
      });
  }

  function removeOwner(u_id) {
    axios
      .post(`${url}/channel/removeowner`, {
        token,
        channel_id,
        u_id,
      })
      .then(() => {
        fetchChannelData(channel_id, token);
      })
      .catch((err) => {
        console.error(err);
        toast.error(DEFAULT_ERROR_TEXT);
      });
  }

  function userIsMember(members) {
    console.log(members);
    return members.find((member) => member.u_id === u_id) !== undefined;
  }

  function userIsOwner(owners, u_id) {
    return owners.find((owner) => owner.u_id === u_id) !== undefined;
  }
  const viewerIsOwner = userIsOwner(owners, u_id);
  return (
    <>
      <Typography variant="h4">{name.toUpperCase()}</Typography>
      <List subheader={<ListSubheader>Members</ListSubheader>}>
        {members.map(({ u_id, name_first, name_last }) => (
          <ListItem key={u_id}>
            <ListItemIcon>
              <Avatar>
                {name_first[0]}
                {name_last[0]}
              </Avatar>
            </ListItemIcon>
            <ListItemText
              primary={
                <>
                  <Grid container alignItems="center" spacing={1}>
                    <Grid item>
                      <Link
                        href={`/profile/${u_id}`}
                      >{`${name_first} ${name_last}`}</Link>
                      {`${userIsOwner(owners, u_id) ? ' ⭐' : ' '}`}
                    </Grid>
                    {viewerIsOwner && (
                      <Grid item>
                        {userIsOwner(owners, u_id) ? (
                          <IconButton
                            size="small"
                            onClick={() => removeOwner(u_id)}
                          >
                            <PersonAddDisabled />
                          </IconButton>
                        ) : (
                          <IconButton
                            size="small"
                            onClick={() => addOwner(u_id)}
                          >
                            <PersonAdd />
                          </IconButton>
                        )}
                      </Grid>
                    )}
                  </Grid>
                </>
              }
            />
          </ListItem>
        ))}
        <ListItem key="invite_member">
          {userIsMember(members) ? (
            <Grid container spacing={1}>
              <Grid item>
                <AddMemberDialog channel_id={channel_id} />
              </Grid>
              <Grid item>
                <Button
                  variant="outlined"
                  onClick={() => leaveChannel(channel_id, token)}
                >
                  Leave Channel
                </Button>
              </Grid>
            </Grid>
          ) : (
            <Button
              variant="outlined"
              color="primary"
              onClick={() => joinChannel(channel_id, token)}
            >
              Join Channel
            </Button>
          )}
        </ListItem>
      </List>
      <ChannelMessages channel_id={channel_id} />
    </>
  );
}

export default Channel;
