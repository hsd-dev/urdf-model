package de.fraunhofer.ipa.jsonschema.generator;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;

import org.eclipse.emf.ecore.EPackage;

import com.fasterxml.jackson.databind.JsonNode;

import kinematics.KinematicsPackage;

import org.apache.commons.cli.*;

public class JsonSchemaConverterApp {

	private static Options options;
	private static CommandLineParser parser;
	private static HelpFormatter helper;

	private static void buildProgramOptions() {
		options = new Options();

		Option output = Option.builder("o").longOpt("output")
				.argName("output")
				.hasArg()
				.required(true)
				.desc("set output path for generated Json schema").build();
		options.addOption(output);

		parser = new DefaultParser();
		helper = new HelpFormatter();
	}

	private static void writeToFile(String filename, String text) {
		FileOutputStream outputStream = null;
		try {
			outputStream = new FileOutputStream(filename);
			byte[] strToBytes = text.getBytes();
			outputStream.write(strToBytes);

			outputStream.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			System.exit(0);
		} catch (IOException e) {
			e.printStackTrace();
			System.exit(0);
		}
	}

	public static void main(String[] args) {
		CommandLine cmd;
		buildProgramOptions();

		String filename = null;
		try {
			cmd = parser.parse(options, args);
			if (cmd.hasOption("o")) {
				filename = cmd.getOptionValue("output");
			}
		} catch (ParseException e) {
			System.out.println(e.getMessage());
			helper.printHelp("Usage:", options);
			System.exit(0);
		}

		DefaultJsonSchemaConverter jsonSchemaCreator = new DefaultJsonSchemaConverter();

		EPackage ePackage = KinematicsPackage.eINSTANCE;
		final JsonNode jsonSchema = jsonSchemaCreator.from(ePackage);

		writeToFile(filename, jsonSchema.toPrettyString());
	}
}
