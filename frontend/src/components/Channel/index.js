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
import AddMemberDialog from './AddMemberDialog';
import ChannelMessages from './ChannelMessages';
import AuthContext from '../../AuthContext';
import { extractUId } from '../../utils/token';
import { useInterval } from '../../utils';
import { pollingInterval, getIsPolling, subscribeToStep, unsubscribeToStep } from '../../utils/update';

function Channel({ channel_id, ...props }) {
  const [name, setName] = React.useState('');
  const [members, setMembers] = React.useState([]);
  const [owners, setOwners] = React.useState([]);
  const token = React.useContext(AuthContext);
  const u_id = extractUId(token);

  function fetchChannelData() {
    axios
      .get('/channel/details', {
        params: {
          token,
          channel_id,
        },
      })
      .then(({ data }) => {
        const { name, owner_members, all_members } = data;
        // assumes members of form [{ u_id, name_first, name_last }]
        setMembers(all_members);
        setOwners(owner_members);
        setName(name);
      })
      .catch((err) => {});
  }

  React.useEffect(() => {
    fetchChannelData();
    subscribeToStep(fetchChannelData);
    return () => unsubscribeToStep(fetchChannelData);
  }, [channel_id, token])

  useInterval(() => {
    if (getIsPolling()) fetchChannelData();
  }, pollingInterval * 2);


  function joinChannel(channel_id, token) {
    axios
      .post('/channel/join', {
        token,
        channel_id,
      })
      .then(() => {
        fetchChannelData(channel_id, token);
      })
      .catch((err) => {});
  }

  function leaveChannel(channel_id, token) {
    axios
      .post('/channel/leave', {
        token,
        channel_id,
      })
      .then(() => {
        fetchChannelData(channel_id, token);
      })
      .catch((err) => {});
  }

  function addOwner(u_id) {
    axios
      .post('/channel/addowner', {
        token,
        channel_id,
        u_id,
      })
      .then(() => {
        fetchChannelData(channel_id, token);
      })
      .catch((err) => {});
  }

  function removeOwner(u_id) {
    axios
      .post('/channel/removeowner', {
        token,
        channel_id,
        u_id,
      })
      .then(() => {
        fetchChannelData(channel_id, token);
      })
      .catch((err) => {});
  }

  function userIsMember(members) {
    return members.find((member) => parseInt(member.u_id,10) === parseInt(u_id,10)) !== undefined;
  }

  function userIsOwner(owners, u_id) {
    return owners.find((owner) => parseInt(owner.u_id,10) === parseInt(u_id,10)) !== undefined;
  }

  const viewerIsOwner = userIsOwner(owners, u_id);

  return (
    <>
      <Typography variant="h4">{name.toUpperCase()}</Typography>
      <List subheader={<ListSubheader>Members</ListSubheader>}>
        {members.map(({ u_id, name_first, name_last, profile_img_url }) => (
          <ListItem key={u_id}>
            <ListItemIcon>
              <img className="avatar-small" src={profile_img_url} />
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
