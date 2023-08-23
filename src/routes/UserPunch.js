import React, { useState, useEffect, Component } from 'react';
import {
    SafeAreaView,
    ScrollView,
    StatusBar,
    StyleSheet,
    Text,
    TextInput,
    useColorScheme,
    View,
    Colors,
    Button,
    Alert,
    fontcolor,
    TouchableOpacity,
} from 'react-native';
import React, { useState } from 'react';
import { View, TextInput, Button, Alert } from 'react-native';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

export default function UserPunch({ navigation }) {
  const [empId, setEmpId] = useState('');

  const handleClockIn = async () => {
    if (empId !== '') {
      try {
        const response = await axios.post(`${API_URL}perform_clock_in/`, {
          emp_id: empId,
        });

        if (response.data.new_session) {
          navigation.navigate('JobPunch', { empId });
        } else {
          // If already clocked in, perform clock out
          const clockOutResponse = await axios.post(`${API_URL}perform_clock_out/`, {
            emp_id: empId,
          });

          if (clockOutResponse.data.message === 'Clock out successful') {
            Alert.alert('Clock Out', 'You have been clocked out');
          }
        }
      } catch (error) {
        // Handle error if necessary
        console.log('Error performing clock in:', error);
      }
    }
  };



  
    const [date, setDate] = React.useState(null);
    const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"];
    const [time, setTime] = React.useState(null);

    const getCurrentTime = () => {
        let today = new Date();
        let hours = (today.getHours() < 10 ? '0' : '') + today.getHours();
        let minutes = (today.getMinutes() < 10 ? '0' : '') + today.getMinutes();
        let seconds = (today.getSeconds() < 10 ? '0' : '') + today.getSeconds();
        return hours + ':' + minutes + ':' + seconds;
    };

    const getCurrentDate = () => {
        let today = new Date();
        let month = monthNames[today.getMonth()];
        let day = today.getDate();
        let year = today.getFullYear();
        return month + " " + day + " " + year
    };

    useEffect(() => {
        let today = new Date();
        let date = getCurrentDate();
        setDate(date);
        let time = getCurrentTime();
        setTime(time);
        let options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };

        const timer = setInterval(() => {
            setTime(new Date().toLocaleTimeString());
            setDate(new Date().toLocaleDateString('en-US', options).replaceAll(',', ''));
        }, 1000);

        return () => {
            clearInterval(timer);
        };
    })


    return (
        <SafeAreaView style={styles.container}>
            <View style={styles.box}>
                <View style={styles.date}>
                    <Text style={styles.datetitle}>
                        {date}
                    </Text>
                </View>
                <View style={styles.time}>
                    <Text style={styles.timetitle}>
                        {time}
                    </Text>
                </View>
                <View style={styles.textbox}>
                    <Text style={styles.title}>
                        User ID:
                    </Text>
                    <TextInput style={styles.input}
                        value={empId}
                        onChangeText={setEmpId}
                        keyboardType="numeric"
                    />
                </View>
                <View style={styles.button}>
                    <Button style={styles.buttons} onPress={handleClockIn}
                        title="Clock In/Out"
                    />
                    <Button style={styles.buttons} onPress={() => navigation.navigate('JobPunch')}
                        title="Switch Jobs"
                    />
                </View>
            </View>
        </SafeAreaView>
    );
    
}

export { EnterEmpIdScreen };

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        backgroundColor: 'black',
        width: '100%',
        height: '100%',
        alignItems: 'center'
    },
    box: {
        flexDirection: 'column',
        backgroundColor: '#001C55',
        alignItems: 'center',
        width: '70%',
        height: '70%',
    },
    title: {
        color: 'white',
        fontSize: 50
    },
    datetitle: {
        color: 'white',
        fontSize: 80
    },
    timetitle: {
        color: 'white',
        fontSize: 100
    },
    date: {
        flex: 2,
        paddingTop: 100,
    },
    time: {
        flex: 2,
    },
    textbox: {
        flex: 1,
        flexDirection: 'row',
        alignItems: 'center'
    },
    input: {
        height: 50,
        width: 100,
        borderWidth: 1,
        marginLeft: 20,
        marginTop: 10,
        textAlign: 'center',
        fontSize: 25,
        justifyContent: 'center', //Centered horizontally
        alignItems: 'center', //Centered vertically

    },
    button: {
        flex: 1,
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center', //Centered vertically

    },
    buttons: {
        width: 150,
        height: 50,
        backgroundColor: 'gray',
        justifyContent: 'center',
        alignItems: 'center',
        fontSize: 25
    }

});
