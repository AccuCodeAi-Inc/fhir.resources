from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DataElement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DataElement(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource data element.
    The formal description of a single piece of information that can be
    gathered and reported.
    """

    __resource_type__ = "DataElement"

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        default=None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    copyright: fhirtypes.MarkdownType | None = Field(  # type: ignore
        default=None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the data element and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the data element."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the data element was published. "
            "The date must change if and when the business version changes and it "
            "must change if the status code changes. In addition, it should change "
            "when the substantive content of the data element changes."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_date", title="Extension field for ``date``."
    )

    element: typing.List[fhirtypes.ElementDefinitionType] = Field(  # type: ignore
        default=...,
        alias="element",
        title="Definition of element",
        description=(
            "Defines the structure, type, allowed values and other constraining "
            "characteristics of the data element."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    experimental: bool | None = Field(  # type: ignore
        default=None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A boolean value to indicate that this data element is authored for "
            "testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_experimental",
        title="Extension field for ``experimental``.",
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Additional identifier for the data element",
        description=(
            "A formal identifier that is used to identify this data element when it"
            " is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    jurisdiction: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="jurisdiction",
        title="Intended jurisdiction for data element (if applicable)",
        description=(
            "A legal or geographic region in which the data element is intended to "
            "be used."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    mapping: typing.List[fhirtypes.DataElementMappingType] | None = Field(  # type: ignore
        default=None,
        alias="mapping",
        title="External specification mapped to",
        description=(
            "Identifies a specification (other than a terminology) that the "
            "elements which make up the DataElement have some correspondence with."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="Name for this data element (computer friendly)",
        description=(
            "A natural language name identifying the data element. This name should"
            " be usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the data "
            "element."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_publisher", title="Extension field for ``publisher``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this data element. Enables tracking the life-cycle of "
            "the content."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    stringency: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="stringency",
        title=(
            "comparable | fully-specified | equivalent | convertable | scaleable | "
            "flexible"
        ),
        description="Identifies how precise the data element is in its definition.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "comparable",
                "fully-specified",
                "equivalent",
                "convertable",
                "scaleable",
                "flexible",
            ],
        },
    )
    stringency__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_stringency", title="Extension field for ``stringency``."
    )

    title: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="title",
        title="Name for this data element (human friendly)",
        description="A short, descriptive, user-friendly title for the data element.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        default=None,
        alias="url",
        title="Logical URI to reference this data element (globally unique)",
        description=(
            "An absolute URI that is used to identify this data element when it is "
            "referenced in a specification, model, design or an instance. This "
            "SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at"
            " which this data element is (or will be) published. The URL SHOULD "
            "include the major version of the data element. For more information "
            "see [Technical and Business Versions](resource.html#versions)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        default=None,
        alias="useContext",
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching for appropriate data element instances."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="version",
        title="Business version of the data element",
        description=(
            "The identifier that is used to identify this version of the data "
            "element when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the data element "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions can be placed in"
            " a lexicographical sequence."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``DataElement`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "url",
            "identifier",
            "version",
            "status",
            "experimental",
            "date",
            "publisher",
            "name",
            "title",
            "contact",
            "useContext",
            "jurisdiction",
            "copyright",
            "stringency",
            "mapping",
            "element",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``DataElement`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "url",
            "identifier",
            "version",
            "status",
            "experimental",
            "date",
            "publisher",
            "name",
            "title",
            "contact",
            "useContext",
            "jurisdiction",
            "stringency",
            "element",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields


class DataElementMapping(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    External specification mapped to.
    Identifies a specification (other than a terminology) that the elements
    which make up the DataElement have some correspondence with.
    """

    __resource_type__ = "DataElementMapping"

    comment: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="comment",
        title="Versions, issues, scope limitations, etc.",
        description=(
            "Comments about this mapping, including version notes, issues, scope "
            "limitations, and other important notes for usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_comment", title="Extension field for ``comment``."
    )

    identity: fhirtypes.IdType | None = Field(  # type: ignore
        default=None,
        alias="identity",
        title="Internal id when this mapping is used",
        description=(
            "An internal id that is used to identify this mapping set when specific"
            " mappings are made on a per-element basis."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    identity__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_identity", title="Extension field for ``identity``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="Names what this mapping refers to",
        description="A name for the specification that is being mapped to.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    uri: fhirtypes.UriType | None = Field(  # type: ignore
        default=None,
        alias="uri",
        title="Identifies what this mapping refers to",
        description=(
            "An absolute URI that identifies the specification that this mapping is"
            " expressed to."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_uri", title="Extension field for ``uri``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``DataElementMapping`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identity",
            "uri",
            "name",
            "comment",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``DataElementMapping`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("identity", "identity__ext")]
        return required_fields
