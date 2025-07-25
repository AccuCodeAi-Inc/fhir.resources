from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicationDispense
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class MedicationDispense(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dispensing a medication to a named patient.
    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """

    __resource_type__ = "MedicationDispense"

    authorizingPrescription: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="authorizingPrescription",
        title="Medication order that authorizes the dispense",
        description="Indicates the medication order that is being dispensed against.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicationRequest"],
        },
    )

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="basedOn",
        title="Plan that is fulfilled by this dispense",
        description=(
            "A plan that is fulfilled in whole or in part by this "
            "MedicationDispense."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CarePlan"],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="category",
        title="Type of medication dispense",
        description=(
            "Indicates the type of medication dispense (for example, drug "
            "classification like ATC, where meds would be administered, legal "
            "category of the medication.)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    daysSupply: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="daysSupply",
        title="Amount of medication expressed as a timing amount",
        description="The amount of medication expressed as a timing amount.",
        json_schema_extra={
            "element_property": True,
        },
    )

    destination: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="destination",
        title="Where the medication was/will be sent",
        description=(
            "Identification of the facility/location where the medication was/will "
            "be shipped to, as part of the dispense event."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    dosageInstruction: typing.List[fhirtypes.DosageType] | None = Field(  # type: ignore
        default=None,
        alias="dosageInstruction",
        title=(
            "How the medication is to be used by the patient or administered by the"
            " caregiver"
        ),
        description="Indicates how the medication is to be used by the patient.",
        json_schema_extra={
            "element_property": True,
        },
    )

    encounter: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="encounter",
        title="Encounter associated with event",
        description="The encounter that establishes the context for this event.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    eventHistory: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="eventHistory",
        title="A list of relevant lifecycle events",
        description=(
            "A summary of the events of interest that have occurred, such as when "
            "the dispense was verified."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Provenance"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="External identifier",
        description=(
            "Identifiers associated with this Medication Dispense that are defined "
            "by business processes and/or used to refer to it when a direct URL "
            "reference to the resource itself is not appropriate. They are business"
            " identifiers assigned to this resource by the performer or other "
            "systems and remain constant as the resource is updated and propagates "
            "from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="location",
        title="Where the dispense occurred",
        description="The principal physical location where the dispense was performed.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    medication: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        default=...,
        alias="medication",
        title="What medication was supplied",
        description=(
            "Identifies the medication supplied. This is either a link to a "
            "resource representing the details of the medication or a simple "
            "attribute carrying a code that identifies the medication from a known "
            "list of medications."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Medication"],
        },
    )

    notPerformedReason: fhirtypes.CodeableReferenceType | None = Field(  # type: ignore
        default=None,
        alias="notPerformedReason",
        title="Why a dispense was not performed",
        description="Indicates the reason why a dispense was not performed.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["DetectedIssue"],
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        default=None,
        alias="note",
        title="Information about the dispense",
        description=(
            "Extra information about the dispense that could not be conveyed in the"
            " other attributes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    partOf: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="partOf",
        title="Event that dispense is part of",
        description=(
            "The procedure or medication administration that triggered the " "dispense."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Procedure", "MedicationAdministration"],
        },
    )

    performer: typing.List[fhirtypes.MedicationDispensePerformerType] | None = Field(  # type: ignore
        default=None,
        alias="performer",
        title="Who performed event",
        description="Indicates who or what performed the event.",
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="quantity",
        title="Amount dispensed",
        description=(
            "The amount of medication that has been dispensed. Includes unit of "
            "measure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    receiver: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="receiver",
        title="Who collected the medication or where the medication was delivered",
        description=(
            "Identifies the person who picked up the medication or the location of "
            "where the medication was delivered.  This will usually be a patient or"
            " their caregiver, but some cases exist where it can be a healthcare "
            "professional or a location."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "Practitioner",
                "RelatedPerson",
                "Location",
                "PractitionerRole",
            ],
        },
    )

    recorded: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="recorded",
        title="When the recording of the dispense started",
        description=(
            "The date (and maybe time) when the dispense activity started if "
            "whenPrepared or whenHandedOver is not populated."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_recorded", title="Extension field for ``recorded``."
    )

    renderedDosageInstruction: fhirtypes.MarkdownType | None = Field(  # type: ignore
        default=None,
        alias="renderedDosageInstruction",
        title="Full representation of the dosage instructions",
        description=(
            "The full representation of the dose of the medication included in all "
            "dosage instructions.  To be used when multiple dosage instructions are"
            " included to represent complex dosing such as increasing or tapering "
            "doses."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    renderedDosageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_renderedDosageInstruction",
        title="Extension field for ``renderedDosageInstruction``.",
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title=(
            "preparation | in-progress | cancelled | on-hold | completed | entered-"
            "in-error | stopped | declined | unknown"
        ),
        description="A code specifying the state of the set of dispense events.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "preparation",
                "in-progress",
                "cancelled",
                "on-hold",
                "completed",
                "entered-in-error",
                "stopped",
                "declined",
                "unknown",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    statusChanged: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="statusChanged",
        title="When the status changed",
        description=(
            "The date (and maybe time) when the status of the dispense record "
            "changed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    statusChanged__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_statusChanged",
        title="Extension field for ``statusChanged``.",
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        default=...,
        alias="subject",
        title="Who the dispense is for",
        description=(
            "A link to a resource representing the person or the group to whom the "
            "medication will be given."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    substitution: fhirtypes.MedicationDispenseSubstitutionType | None = Field(  # type: ignore
        default=None,
        alias="substitution",
        title="Whether a substitution was performed on the dispense",
        description=(
            "Indicates whether or not substitution was made as part of the "
            "dispense.  In some cases, substitution will be expected but does not "
            "happen, in other cases substitution is not expected but does happen.  "
            "This block explains what substitution did or did not happen and why.  "
            "If nothing is specified, substitution was not done."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    supportingInformation: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="supportingInformation",
        title="Information that supports the dispensing of the medication",
        description=(
            "Additional information that supports the medication being dispensed.  "
            "For example, there may be requirements that a specific lab test has "
            "been completed prior to dispensing or the patient's weight at the time"
            " of dispensing is documented."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="Trial fill, partial fill, emergency fill, etc",
        description=(
            "Indicates the type of dispensing event that is performed. For example,"
            " Trial Fill, Completion of Trial, Partial Fill, Emergency Fill, "
            "Samples, etc."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    whenHandedOver: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="whenHandedOver",
        title="When product was given out",
        description=(
            "The time the dispensed product was provided to the patient or their "
            "representative."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    whenHandedOver__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_whenHandedOver",
        title="Extension field for ``whenHandedOver``.",
    )

    whenPrepared: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="whenPrepared",
        title="When product was packaged and reviewed",
        description="The time when the dispensed product was packaged and reviewed.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    whenPrepared__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_whenPrepared",
        title="Extension field for ``whenPrepared``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``MedicationDispense`` according to specification,
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
            "identifier",
            "basedOn",
            "partOf",
            "status",
            "notPerformedReason",
            "statusChanged",
            "category",
            "medication",
            "subject",
            "encounter",
            "supportingInformation",
            "performer",
            "location",
            "authorizingPrescription",
            "type",
            "quantity",
            "daysSupply",
            "recorded",
            "whenPrepared",
            "whenHandedOver",
            "destination",
            "receiver",
            "note",
            "renderedDosageInstruction",
            "dosageInstruction",
            "substitution",
            "eventHistory",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``MedicationDispense`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "modifierExtension",
            "status",
            "medication",
            "subject",
            "whenPrepared",
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


class MedicationDispensePerformer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who performed event.
    Indicates who or what performed the event.
    """

    __resource_type__ = "MedicationDispensePerformer"

    actor: fhirtypes.ReferenceType = Field(  # type: ignore
        default=...,
        alias="actor",
        title="Individual who was performing",
        description=(
            "The device, practitioner, etc. who performed the action.  It should be"
            " assumed that the actor is the dispenser of the medication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
                "Patient",
                "Device",
                "RelatedPerson",
                "CareTeam",
            ],
        },
    )

    function: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="function",
        title="Who performed the dispense and what they did",
        description=(
            "Distinguishes the type of performer in the dispense.  For example, "
            "date enterer, packager, final checker."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``MedicationDispensePerformer`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "function", "actor"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``MedicationDispensePerformer`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]


class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether a substitution was performed on the dispense.
    Indicates whether or not substitution was made as part of the dispense.  In
    some cases, substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.  If nothing is specified,
    substitution was not done.
    """

    __resource_type__ = "MedicationDispenseSubstitution"

    reason: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="reason",
        title="Why was substitution made",
        description=(
            "Indicates the reason for the substitution (or lack of substitution) "
            "from what was prescribed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    responsibleParty: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="responsibleParty",
        title="Who is responsible for the substitution",
        description=(
            "The person or organization that has primary responsibility for the "
            "substitution."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title=(
            "Code signifying whether a different drug was dispensed from what was "
            "prescribed"
        ),
        description=(
            "A code signifying whether a different drug was dispensed from what was"
            " prescribed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    wasSubstituted: bool | None = Field(  # type: ignore
        default=None,
        alias="wasSubstituted",
        title="Whether a substitution was or was not performed on the dispense",
        description=(
            "True if the dispenser dispensed a different drug or product from what "
            "was prescribed."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    wasSubstituted__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_wasSubstituted",
        title="Extension field for ``wasSubstituted``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``MedicationDispenseSubstitution`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "wasSubstituted",
            "type",
            "reason",
            "responsibleParty",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``MedicationDispenseSubstitution`` according to specification,
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
        required_fields = [("wasSubstituted", "wasSubstituted__ext")]
        return required_fields
