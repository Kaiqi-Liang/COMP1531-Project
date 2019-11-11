import React from 'react';
import Layout from '../components/Layout';
import ProfileChannelLists from '../components/ProfileChannelLists';
import Slack from '../slack.jpg'
import { Typography } from '@material-ui/core';

function HomePage(props) {
  return (
    <Layout
      menu={<ProfileChannelLists />}
      body={
        <>
          <Typography variant="h4"> WELCOME TO SLACKR ❤️ </Typography>
          <div>
            <img src={Slack} />
          </div>
        </>
      }
    />
  );
}

export default HomePage;
