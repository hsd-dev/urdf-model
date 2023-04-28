package de.fraunhofer.ipa.jsonschema.generator;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;

import com.fasterxml.jackson.databind.JsonNode;

import org.apache.commons.cli.*;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.emf.ecore.xmi.impl.EcoreResourceFactoryImpl;

public class JsonSchemaConverterApp {

	private static Options options;
	private static CommandLineParser parser;
	private static HelpFormatter helper;

	private static void buildProgramOptions() {
		options = new Options();

		Option ecore = Option.builder("e").longOpt("ecore")
				.argName("ecore_file")
				.hasArg()
				.required(true)
				.desc("set ecore file path from which Json schema is to be generated").build();
		options.addOption(ecore);

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

		String ecore = null;
		String filename = null;
		try {
			cmd = parser.parse(options, args);
			if (cmd.hasOption("e")) {
				ecore = cmd.getOptionValue("ecore");
			}
			if (cmd.hasOption("o")) {
				filename = cmd.getOptionValue("output");
			}
		} catch (ParseException e) {
			System.out.println(e.getMessage());
			helper.printHelp("Usage:", options);
			System.exit(0);
		}

		ResourceSet resourceSet = new ResourceSetImpl();
		resourceSet.getResourceFactoryRegistry().getExtensionToFactoryMap().put("ecore",
				new EcoreResourceFactoryImpl());
		URI uri = URI.createFileURI(ecore);
		Resource resource = resourceSet.getResource(uri, true);
		EObject object = resource.getContents().get(0);

		DefaultJsonSchemaConverter jsonSchemaCreator = new DefaultJsonSchemaConverter();
		final JsonNode jsonSchema = jsonSchemaCreator.from(object);

		writeToFile(filename, jsonSchema.toPrettyString());
	}
}
