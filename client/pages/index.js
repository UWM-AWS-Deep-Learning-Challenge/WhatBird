import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";
const axios = require("axios");
import { useState, useEffect } from "react";
import {
  Box,
  Heading,
  Center,
  Text,
  Input,
  VStack,
  HStack,
  Button,
} from "@chakra-ui/react";

export default function Home() {
  const [filePaths, setFilePaths] = useState({});
  const [userInputNum, setUserInputNum] = useState();
  const [results, setResults] = useState([]);
  const [modal, changeModal] = useState(1);

  const handleChange = (e) => setUserInputNum(e.target.value);

  const submitButton = () => {
    axios
      .post("/production/get_valid_files", {
        numberOfFiles: userInputNum,
      })
      .then(function (response) {
        setFilePaths(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    changeModal(2);
  };

  const predictButton = () => {
    for (const file in filePaths) {
      axios
        .post("/production/fileToPredict", {
          fileToPredict: filePaths[file],
        })
        .then(function (response) {
          setResults([...results, response]);
        })
        .catch(function (error) {
          console.log(error);
        });
    }

    changeModal(3);
  };

  const restartButton = () => {
    changeModal(1);
  };

  return (
    <Box>
      {modal == 1 ? (
        <Center mt={52}>
          {" "}
          <VStack>
            <Heading fontSize={"90"}>What Bird?</Heading>
            <Input
              onChange={handleChange}
              placeholder={"Enter number of birds to predict less than 10"}
            />

            <Button
              bg={"black"}
              color={"white"}
              w={"100%"}
              onClick={() => submitButton()}
            >
              Submit
            </Button>
          </VStack>
        </Center>
      ) : modal == 2 ? (
        <Center mt={52}>
          {" "}
          <VStack spacing={8}>
            <Heading fontSize={"90"}>Birds To Predict</Heading>
            <HStack>
              <Box border={"1px solid black"} h={"60"} w={"80"}></Box>
              <Box border={"1px solid black"} h={"60"} w={"80"}></Box>
              <Box border={"1px solid black"} h={"60"} w={"80"}></Box>
              <Box border={"1px solid black"} h={"60"} w={"80"}></Box>
            </HStack>

            <Button
              bg={"black"}
              color={"white"}
              w={"100%"}
              onClick={() => predictButton()}
            >
              Predict
            </Button>
          </VStack>
        </Center>
      ) : (
        <Center mt={52}>
          {" "}
          <VStack spacing={4}>
            <Heading fontSize={"90"}>Predictions</Heading>
            <Center>
              <Box border={"1px solid black"} h={"60"} w={"80"}></Box>
            </Center>
            <HStack spacing={4}>
              <Box border={"1px solid black"} h={"60"} w={"80"}></Box>
              <Box border={"1px solid black"} h={"60"} w={"80"}></Box>
              <Box border={"1px solid black"} h={"60"} w={"80"}></Box>
            </HStack>

            <HStack spacing={4}>
              <Box border={"1px solid black"} h={"10"} w={"80"}>
                <Text fontWeight={"bold"} align={"center"}>
                  Confidence: 40
                </Text>
              </Box>
              <Box border={"1px solid black"} h={"10"} w={"80"}>
                <Text fontWeight={"bold"} align={"center"}>
                  Confidence: 40
                </Text>
              </Box>
              <Box border={"1px solid black"} h={"10"} w={"80"}>
                <Text fontWeight={"bold"} align={"center"}>
                  Confidence: 40
                </Text>
              </Box>
            </HStack>
            <Button
              bg={"black"}
              color={"white"}
              w={"100%"}
              onClick={() => restartButton()}
            >
              Restart
            </Button>
          </VStack>
        </Center>
      )}
    </Box>
  );
}
