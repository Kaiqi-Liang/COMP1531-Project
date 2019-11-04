import React from 'react';
import Layout from '../components/Layout';
import ProfileChannelLists from '../components/ProfileChannelLists';
import Slack from '../slack.png'
import { Typography } from '@material-ui/core';

function HomePage(props) {
  return (
    <Layout
      menu={<ProfileChannelLists />}
      body={
        <>
          <Typography variant="h4">WELCOME</Typography>
          <div style={{ paddingTop: 15 }}>
            <Typography variant="body1">
              This is SAKE: Welcome to our Slackr ❤️
            </Typography>
          </div>
          <div>
            <img src={Slack} />
          </div>
        </>
      }
    />
  );
}

export default HomePage;
